# Understanding this Repo
If you are helping maintain this repo, or you're just curious about how this repo operates behind the scenes, this is the file to read.

Below, you'll find information about this repo's actions, issue forms, and other scripts.

## Why the Change?
Why did we change how the repo works. We did it for two reasons:
1) We wanted to make sure technical challenges were not an obstacle that prevented people from contributing. Instead of needing to fork the repo, make a markdown row, and make a pr, now you simply need to fill out an issue form to contribute.
2) We added a script that automatically adds all technical internships from Simplify's database onto this repo, so we needed to systematize the whole process to combine these internships with contributors' internships.

## High Level Overview

### listings.json

All internships (from Simplify and contributors) are stored in `.github/scripts/listings.json.` A list entry for an internship might look like the following:

```json
{
        "company_name": "Capital One",
        "locations": [
            "McLean, VA",
            "Plano, TX"
        ],
        "title": "Product Development Intern (No Sponsorship)",
        "date_posted": "05/12/2023",
        "terms": [
            "Summer 2024"
        ],
        "active": true,
        "url": "https://www.capitalonecareers.com/job/mclean/product-development-intern-summer-2024/31238/51746418592",
        "is_visible": true,
        "source": "Markdown",
        "company_url": "",
        "date_updated": "07/27/2023",
        "id": "98b2d671-3f03-430e-b18c-e5ddb8ce5035"
    },
```

The schema of this files is as follows:

# | Property Name   | Data Type        | Description                                          | Example |
# | --------------- | ---------------- | ---------------------------------------------------- | -------- |
# | **company_name**| `str`            | Name of company                                      | Google |
# | **company_url**  | `str`            | Start date of internship (format: MM/DD/YYYY)        | 06/15/2024 |
# | **title**       | `str`            | Name of internship position                          | ML Software Engineer Intern |
# | **date_posted**  | `str`            | Start date of internship (format: MM/DD/YYYY)        | 06/15/2024 |
# | **date_updated** | `str`            | Start date of internship (format: MM/DD/YYYY)        | 06/15/2024 |
# | **url**         | `str`            | Link to job posting (include "https://")             | https://google.com/link/to/job/posting |
# | **terms**   | `[str]`          | Array of locations available for internship | ["Mountain View, CA", "Remote"] |
# | **locations**   | `[str]`          | Array of locations available for internship | ["Mountain View, CA", "Remote"] |
# | **active**      | `bool`           | `true` if application is open. `false` if not.         | true |
# | **is_visible**      | `bool`           | `true` if application is open. `false` if not.         | true |
# | **source**      | `str`           | `true` if application is open. `false` if not.         | true |
# | **id**      | `str`           | `true` if application is open. `false` if not.         | true |

## Github issue templates

In 

## Github action

The github action is responsible for adding new contributions and edits to `listings.json`
> Note that it does not directly edit any README files. Only the listings.json file.
The github action runs every time a new label is added to an issue. However, it skips every run except for those where the label added is the "approved" label. 

## Adding an Internship
Cool! You're ready to add an internship to the list. Follow these steps:

1) First create a new issue [here](https://github.com/pittcsc/Summer2024-Internships/issues/new/choose).
2) Select the **New Internship** issue template.
3) Fill in the information about your internship into the form, then hit submit.
> Please make a new submission for each unique position, **even if they are for the same company**.
4) That's it! Once a member of our team has reviewed your submission, it will be automatically added to the correct `README`

## Editing an Internship
To edit an internship (changing name, setting as inactive, removing, etc.), follow these steps:
1) First copy the url of the internship you would like to edit.
> This can be found by right-clicking on the `APPLY` button and selecting **copy link address**
2) Create a new issue [here](https://github.com/pittcsc/Summer2024-Internships/issues/new/choose).
3) Select the **Edit Internship** issue template.
4) Fill in the url to the **link** input.
> This is how we ensure your edit affects the correct internship
5) Leave every other input blank except for whichever fields you would like to update or change about the internship.
6) If it is not obvious why you are making these edits, please specify why in the reason box at the bottom of the form.
7) Hit submit. A member of our team will review your revision and approve it shortly.

## Automatic README.md Updates
A script will automatically add new contributions as well as new internships found by [Simplify](https://simplify.jobs) to the appropriate README. The row will look something like this:
```md
| Company | Role | Location | Application | Simplify Application |
| --- | --- | --- | :---: | :---: |
| **[Example Company]()** | Software Engineering Internship Example | San Francisco, CA | <img src="https://i.imgur.com/5JF7mJI.png" width="150" alt="Apply"> |  |
```

When rendered, it will look like:
| Company | Role | Location | Application | Simplify Application |
| --- | --- | --- | :---: | :---: |
| **[Example Company]()** | Software Engineering Internship Example | San Francisco, CA | <img src="https://i.imgur.com/5JF7mJI.png" width="150" alt="Apply"> |  |


