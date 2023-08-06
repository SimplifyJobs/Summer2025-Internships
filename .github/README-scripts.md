# Understanding this Repo
If you are helping maintain this repo, or you're just curious about how this repo operates behind the scenes, this is the file to read.

Below, you'll find information about this repo's actions, issue forms, and other scripts.

## High Level Overview

Internships are stored in `listings.json`. This file is edited by submitting a `new_internship` or `edit_internship` issue form. Once an `approved` label is attached to one of these issues, a github action will run and automatically edit listings.json with the new information. An external microservice runs a separate script once per day which fetches internships from Simplify's database, and also adds them to listings.json. Everytime listings.json is updated (either by the microservice or by github actions) another github action called "Update READMEs" will update the corresponding `README` with the new internships from Simplify and contributors. 

See information about each of these steps below.

## listings.json

All internships (from Simplify and contributors) are stored in `.github/scripts/listings.json.` This file can be edited manually (if you are being careful) or through a github action by approving an issue (see below). A list entry for an internship might look like the following:

```json
[
    {
        "company_name": "Capital One",
        "locations": [
            "McLean, VA",
            "Plano, TX"
        ],
        "title": "Product Development Intern (No Sponsorship)",
        "date_posted": 1690430400,
        "terms": [
            "Summer 2024"
        ],
        "active": true,
        "url": "https://www.capitalonecareers.com/job/mclean/product-development-intern-summer-2024/31238/51746418592",
        "is_visible": true,
        "source": "Markdown",
        "company_url": "",
        "date_updated": 1690430400,
        "id": "98b2d671-3f03-430e-b18c-e5ddb8ce5035"
    }
]
```

The schema of this file is as follows:

| Property Name    | Data Type        | Description                                          | Example |
| ---------------  | ---------------- | ---------------------------------------------------- | -------- |
| **company_name** | `str`            | Name of company                                      | Google |
| **company_url**  | `str`            | link to Simplify page for company (is empty string for non-Simplify contributions)       | "simplify.com/c/CompanyName |
| **title**        | `str`            | Name of internship position                          | ML Software Engineer Intern |
| **date_posted**  | `int`            | date added to listings.json (timestamp)        | 1690430400 |
| **date_updated** | `int`            | date updated with new information (timestamp)        | 1690430400 |
| **url**         | `str`            | Link to job posting            | https://google.com/link/to/job/posting |
| **terms**   | `[str]`          | Array of terms available for internship | ["Summer 2024", "Fall 2023"] |
| **locations**   | `[str]`          | Array of locations available for internship | ["Mountain View, CA", "Remote"] |
| **active**      | `bool`           | `true` if application is open. `false` if not.         | true |
| **is_visible**      | `bool`           | `true` if visible in README. `false` if not.         | true |
| **source**      | `str`           | `Simplify` if from Simplfiy. Otherwise the github username of the contributor         | Simplify or michael-scarn |
| **id**      | `str`           | unique id for listing. useful for Simplify listings, meaningless for contributions        | 95411fb3-8e62-4669-a456-9e6939d73e75 |

## Github issue templates

We have a few github issue templates that can be found in `.github/ISSUE_TEMPLATE`

| Name | filename | Purpose | Label |
| ---- | -------- | ------- | ----- |
| New Internship | new_internship.yaml | Form for adding a new internship to listings.json | `new_internship` |
| Edit Internship | edit_internship.yaml | Form for updating information about internship in listings.json | `edit_internship` |
| Miscellaneous Issue | misc.yaml | Form for asking questions, reporting bugs, etc. | `misc` |
| Feature Suggestion | feature_suggestion.yaml | Form for suggesting improvements to the repo | `enhancement` |

> Miscellaneous issues and feature suggestions should be manually handled and closed.

### This is the process for handling New Internship and Edit Internship issues:

1) Review the submission to ensure all the fields look good and the internship fits the theme of the repo.
2) If there are any problems with it, respond to the issue explaining what needs to be changed. The contributor must submit a new issue form with the fixes.
3) If there are no issues. Add the `approved` label to the issue which will cause the github action to run.
4) If there is any issue with the github action, it will respond to the issue with what occured. For more information, you can look in the actions tab on the repo to see why the action failed.
5) If there are no issues with the action, then the issue will be autoclosed and the new internship or edits should be reflected in listings.json.

## Github actions

### Contribution Approved
A github action called "Contribution Approved" is responsible for adding new contributions and edits to `listings.json`
> Note that it does not directly edit any README files, only the listings.json file.

The github action runs every time a new label is added to an issue. However, it skips every run except for those where the label added is the "approved" label.

In `.github/workflows/actions.yml`, you will find the github action. Here is what each step is accomplishing:
1) Checkout repository
2) Set up python
3) Execute `contribution_approved.py`. This file handles most of the logic for the github action. It first extracts the information from the issue form into a python dictionary. For new internships, it will make sure the internship does not already exist in listings.json, then will add it. For edits, the script will find the listing to edit, then make the corresponding edits in listings.json. If there are any errors, this step will fail and the `error_message` output will be set to whatever went wrong. If step 3 fails, steps 4-6 will not run, and the github action will skip to step 7.
4) Assuming step 3 succeeded, the changes to listings.json will be committed. If the used provided their email, the GitHub action will pretend to be that user when adding to listings.json in order to give them credit for contributing to the repo.
5) The changes will be pushed.
6) The issue that sparked this github action will be closed.
7) If any one of these steps fails, this will respond to the issue that spawned this process with the error.


### Update READMEs

This is a separate github action that can be manually run, but it also runs every time a commit is made to listings.json. This github action will reformat the tables in both READMEs to include the updated information in listings.json.

## External Script

There is a private script that runs externally once per day, which will do the following:
1) Pull new internships from Simplify's database.
2) Add these internships to listings.json.

## Miscellaneous information:

- The listings are sorted based on date posted


## Why the Change?
Why did we change how the repo works. We did it for two reasons:
1) We wanted to make sure technical challenges were not an obstacle that prevented people from contributing. Instead of needing to fork the repo, make a markdown row, and make a pr, now you simply need to fill out an issue form to contribute.
2) We added a script that automatically adds all technical internships from Simplify's database onto this repo, so we needed to systematize the whole process to combine these internships with contributors' internships.

