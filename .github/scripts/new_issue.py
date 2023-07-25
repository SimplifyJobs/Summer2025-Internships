import sys
import json
import subprocess
import sys
import uuid
from datetime import datetime


def throwError(message):
    print("::set-output name=error_message::" + message)
    exit(1)


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
    data["location"] = [line.strip() for line in lines[line_i].split("|")]
    line_i = getNextLine(lines, line_i)
    data["terms"] = [line.strip() for line in lines[line_i].split(",")]
    return data


def main():
    event_file_path = sys.argv[1]

    with open(event_file_path) as f:
        event_data = json.load(f)

    issue_number = event_data['issue']['number']
    issue_title = event_data['issue']['title']
    issue_body = event_data['issue']['body']
    issue_user = event_data['issue']['user']['login']

    keys = ["### Company Name", "### Internship Title",
            "### Link to Internship Posting"]

    if all([key in issue_body for key in keys]):
        print("::set-output name=new_internship::true")
    else:
        print("::set-output name=new_internship::false")
        return

    data = getData(issue_body)
    data["source"] = issue_user
    data["id"] = str(uuid.uuid4())
    data["date_updated"] = datetime.now().strftime("%m/%d/%Y")
    data["date_posted"] = datetime.now().strftime("%m/%d/%Y")

    listings = []
    with open(".github/scripts/listings.json", "r") as f:
        listings = json.load(f)

    # for listing in listings:

    with open(".github/scripts/listings.json", "w") as f:
        f.write(json.dumps(issue_body, indent=4))


if __name__ == "__main__":
    main()
