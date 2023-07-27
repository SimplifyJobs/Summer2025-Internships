import sys
import json
import subprocess
import sys
import uuid
from datetime import datetime
import os

def fail(why):
    setOutput("error_message", why)
    exit(1)


def setOutput(key, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
        print(f'{key}={value}', file=fh)


def add_https_to_url(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url


def getData(body, is_edit):
    data = {}
    lines = [text.strip("# ") for text in body.split("\n\n")]
    #["Company Name", "_No response_", "Internship Title", "_No response_", "Link to Internship Posting", "example.com/link/to/posting", "Locatio", "San Franciso, CA | Austin, TX | Remote" ,"What term(s) is this internship offered for?", "_No response_"]
    
    data["date_updated"] = datetime.now().strftime("%m/%d/%Y")

    if "no response" not in lines[1].lower():
        data["url"] = add_https_to_url(lines[1].strip())
    if "no response" not in lines[3].lower():
        data["company_name"] = lines[3]
    if "no response" not in lines[5].lower():
        data["title"] = lines[5]
    if "no response" not in lines[7].lower():
        data["locations"] = [line.strip() for line in lines[7].split("|")]
    if "no response" not in lines[9].lower():
        data["terms"] = [line.strip() for line in lines[9].split(",")]
    if "none" not in lines[11].lower():
        data["active"] = "yes" in lines[11].lower()
    if is_edit:
        data["is_visible"] = "[x]" not in lines[13].lower()

    return data


def main():
    event_file_path = sys.argv[1]

    with open(event_file_path) as f:
        event_data = json.load(f)

    with open("debug.json", "w") as f:
        f.write(json.dumps(event_data, indent=4))

    new_internship = "new_internship" in [label["name"] for label in event_data["issue"]["labels"]]
    edit_internship = "edit_internship" in [label["name"] for label in event_data["issue"]["labels"]]

    edit_approved = all([
        "APPROVED" in event_data['comment']['body'],
        event_data["comment"]["author_association"] in ["OWNER"],
        new_internship or edit_internship
    ])

    if not edit_approved:
        setOutput("edit_approved", "false")
        return
    setOutput("edit_approved", "true")
    
    issue_body = event_data['issue']['body']
    issue_user = event_data['issue']['user']['login']

    data = getData(issue_body, is_edit=edit_internship)
    setOutput("job_description", data["title"] + " at " + data["company"])
    
    if new_internship:
        data["source"] = issue_user
        data["id"] = str(uuid.uuid4())
        data["date_posted"] = datetime.now().strftime("%m/%d/%Y")
        data["company_url"] = ""
        data["is_visible"] = True

    listings = []
    with open("listings.json", "r") as f:
        listings = json.load(f)

    found = next(
        (item for item in listings if item["url"] == data["url"]), None)
    if found:
        if new_internship:
            fail("This internship is already in our list. See CONTRIBUTING.md for how to edit a listing")
        for key, value in data.items():
            found[key] = value
    else:
        if edit_internship:
            fail("We could not find this internship in our list. Please double check you inserted the right url")
        listings.append(data)

    with open("listings.json", "w") as f:
        f.write(json.dumps(listings, indent=4))


if __name__ == "__main__":
    main()
