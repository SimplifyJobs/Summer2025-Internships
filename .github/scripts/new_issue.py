import sys
import json
import subprocess
import sys


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

    values = []
    for line in issue_body.split("\n"):
        values.append(line)
        # if line.find("#") == -1:
        #     values.append(line.strip().lower())

    with open("listings.json", "w") as f:
        f.write(json.dumps(values, indent=4))

    print("::set-output name=new_internship::true")


if __name__ == "__main__":
    main()
