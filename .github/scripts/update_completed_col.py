import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_markdown(filename):
    """
    Load the markdown file and return its content as a list of lines.

    :param filename: The name of the markdown file to load.
    :return: A list of lines from the markdown file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()


def save_markdown(filename, lines):
    """
    Save the provided lines to the markdown file.

    :param filename: The name of the markdown file to save.
    :param lines: The lines to write to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def get_company_name(lines, index):
    """
    Backtrack to find the most recent company name when an arrow (↳) is encountered.

    :param lines: The lines from the markdown file.
    :param index: The current line index.
    :return: The most recent company name.
    """
    company_pattern1 = re.compile(r'\|\s*\[(.*?)\]\s*\|')
    company_pattern2 = re.compile(r'\|\s*\*\*\[(.*?)\]\(.*?\)\*\*\s*\|')

    for i in range(index - 1, -1, -1):
        match1 = company_pattern1.search(lines[i])
        match2 = company_pattern2.search(lines[i])
        if match1:
            return match1.group(1).strip()
        elif match2:
            return match2.group(1).strip()
    return None


def process_markdown(lines):
    """
    Process the markdown file to replace arrow symbols with the closest company name above them.

    :param lines: The lines from the markdown file.
    :return: The processed lines with company names replaced.
    """
    processed_lines = lines[:]
    for i, line in enumerate(lines):
        if '| ↳ |' in line:
            company_name = get_company_name(lines, i)
            if company_name:
                processed_lines[i] = line.replace('↳', company_name)
    return processed_lines


def search_jobs(lines, keywords):
    """
    Search for the job that best matches the provided keywords using TF-IDF and cosine similarity,
    and is not marked as completed.

    :param lines: The lines from the markdown file.
    :param keywords: A list of keywords to search for.
    :return: A tuple containing the index and line of the best match.
    """
    documents = [line for line in lines if re.match(r'\|.*\|', line) and '<span style="color:red">False</span>' in line]

    vectorizer = TfidfVectorizer().fit(documents)
    tfidf_matrix = vectorizer.transform(documents)

    query_vec = vectorizer.transform([' '.join(keywords)])
    cosine_similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()

    best_match_index = np.argmax(cosine_similarities)
    best_match_line = documents[best_match_index]

    for index, line in enumerate(lines):
        if line == best_match_line in line:
            return index, line

    return None, None


def display_job(match):
    """
    Display the matching job to the user.

    :param match: A tuple containing the index and line of the best match.
    """
    if match[1]:
        print(f"Best match:\n{match[1].strip()}")
    else:
        print("No matching job found.")


def mark_job_completed(lines, index):
    """
    Mark a job as completed by setting the "Completed" value to True.

    :param lines: The lines from the markdown file.
    :param index: The index of the line to mark as completed.
    """
    lines[index] = re.sub(r'<span style="color:red">False</span>', '<span style="color:green">True</span>',
                          lines[index])


def main():
    filename = '../../README.md'
    processed_filename = 'processed_README.md'

    lines = load_markdown(filename)
    processed_lines = process_markdown(lines)
    save_markdown(processed_filename, processed_lines)

    # Load the processed markdown for searching
    lines = load_markdown(processed_filename)

    while True:
        # Prompt the user for keywords to search for jobs
        keywords = input("Enter keywords for the job search (comma-separated): ").split(',')
        match = search_jobs(lines, keywords)

        if not match[1]:
            print("No matching jobs found. Please be more specific.")
            continue

        # Display the matching job to the user
        display_job(match)

        confirm = input("Is this the correct job? (yes/no): ").strip().lower()
        if confirm == 'yes':
            # Mark the job as completed and save the file
            mark_job_completed(lines, match[0])
            save_markdown(processed_filename, lines)
            print("Job marked as completed.")
            break
        else:
            print("Please provide more specific keywords.")


if __name__ == "__main__":
    main()
