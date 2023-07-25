import sys
import json
import subprocess
import sys


def getNextLine(lines, curr_i):
    curr_i += 1
    while curr_i < len(lines) and ("#" in lines[curr_i] or len(lines[curr_i]) == 0):
        curr_i += 1
    return curr_i


def add_https_to_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url


def getData(body):
    data = {}
    i = 0
    line_i = 0
    lines = body.split("\n")

    line_i = getNextLine(lines, line_i)
    data["company_name"] = lines[line_i]
    line_i = getNextLine(lines, line_i)
    data["title"] = lines[line_i]
    line_i = getNextLine(lines, line_i)
    data["url"] = add_https_to_url(lines[line_i].strip())
    line_i = getNextLine(lines, line_i)
    data["location"] = [line.strip() for line in lines[line_i].split(";")]
    line_i = getNextLine(lines, line_i)
    data["terms"] = [line.strip() for line in lines[line_i].split(",")]
    return data


def main():
    # Read the file path from the command-line arguments
    event_file_path = sys.argv[1]

    # Load the content of the event file
    with open(event_file_path) as f:
        event_data = json.load(f)

    # Access information about the newly opened issue
    issue_number = event_data['issue']['number']
    issue_title = event_data['issue']['title']
    issue_body = event_data['issue']['body']
    issue_user = event_data['issue']['user']['login']

    # keys = ["company_name", "title", "url", "location", "terms"]
    # for line in issue_body.split("\n"):
    #     values.append(line)
    # if line.find("#") == -1:
    #     values.append(line.strip().lower())

    data = getData(issue_body)

    with open("listings.json", "w") as f:
        f.write(json.dumps(data, indent=4))

    print("::set-output name=new_internship::true")


if __name__ == "__main__":
    main()
