import sys
import json
import subprocess
import sys
import uuid
from datetime import datetime
import os


def throwError(message):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'error_message={message}', file=fh)
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
    data["locations"] = [line.strip() for line in lines[line_i].split("|")]
    line_i = getNextLine(lines, line_i)
    data["terms"] = [line.strip() for line in lines[line_i].split(",")]

    return data


def main():
    event_file_path = sys.argv[1]

    with open(event_file_path) as f:
        event_data = json.load(f)

    with open("listings.json", "w") as f:
        f.write(json.dump(event_data, indent=4))

    return
    issue_number = event_data['issue']['number']
    issue_title = event_data['issue']['title']
    issue_body = event_data['issue']['body']
    issue_user = event_data['issue']['user']['login']
    new_internship = "new_internship" in [
        label["name"] for label in event_data["issue"]["labels"]]

    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'new_internship={new_internship}', file=fh)
    if not new_internship:
        return

    data = getData(issue_body)
    data["source"] = issue_user
    data["id"] = str(uuid.uuid4())
    data["date_updated"] = datetime.now().strftime("%m/%d/%Y")
    data["date_posted"] = datetime.now().strftime("%m/%d/%Y")
    data["active"] = True
    data["company_url"] = ""
    data["is_visible"] = True

    listings = []
    with open("listings.json", "r") as f:
        listings = json.load(f)

    found = next(
        (item for item in listings if item["url"] == data["url"]), None)
    if found:
        throwError(
            "This internship is already in our list. See CONTRIBUTING.md for how to edit a listing")
    else:
        listings.append(data)

    with open("listings.json", "w") as f:
        f.write(json.dumps(listings, indent=4))


if __name__ == "__main__":
    main()
