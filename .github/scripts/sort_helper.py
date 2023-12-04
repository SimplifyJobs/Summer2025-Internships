import re

def sort_internships(readme_content):
    # Find the start and end of the table
    start_marker = "<!-- Please leave a one line gap between this and the table TABLE_START (DO NOT CHANGE THIS LINE) -->"
    end_marker = "<!-- Please leave a one line gap between this and the table TABLE_END (DO NOT CHANGE THIS LINE) -->"

    start_index = readme_content.find(start_marker)
    end_index = readme_content.find(end_marker)

    if start_index == -1 or end_index == -1:
        return readme_content  # Return original content if markers are not found

    # Extract the table content
    table_content = readme_content[start_index:end_index]

    # Split the internships into lines
    lines = table_content.split('\n')

    # Separate open and closed internships
    open_internships = [line for line in lines if '🔒' not in line and line.strip()]
    closed_internships = [line for line in lines if '🔒' in line]

    # Combine the sorted internships
    sorted_internships = '\n'.join(open_internships + closed_internships)

    # Reassemble the README
    sorted_readme = readme_content[:start_index] + sorted_internships + readme_content[end_index:]
    return sorted_readme

# Read the README file content 
with open('README.md', 'r') as file:
    content = file.read()


# Sort the internships
sorted_content = sort_internships(content)

# Write the sorted README back 
with open('README.md', 'w') as file:
    file.write(sorted_content)

