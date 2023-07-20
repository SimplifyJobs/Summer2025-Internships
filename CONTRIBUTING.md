# Contributing to the Internship List
Thank you for your interest in contributing to the Pitt CSC and Simplify internship list!

Below, you'll find the guidelines for our repository. If you have any questions, please create an [issue](https://github.com/pittcsc/Summer2024-Internships/issues/new) here.
> If you're new to using git, check out these guides for [forking a repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and [creating pull-requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

## Finding an Internship to Add
We ask that the internships that you add meet some requirements. Specifically, your internship must
- be in one of the following categories:
    - software/computer engineering,
    - computer/data science,
    - product manager,
    - quant, and
    - any other tech-related internships.
- be located in the United States, Canada, or remote.
- not already exist in the internship list.

## Adding an Internship
Cool! You're ready to add an internship to the list. Follow these steps:

1) Navigate to the file `contributions.json`. It should look something like this.
```jsonc
[
    // example contribution (don't delete)
    {
        "company_name": "ExampleCompany",
        "title": "Software Engineering Internship Example",
        "start_date": "MM/DD/YYYY",
        "url": "https://example.com/this/is/a/link/to/the/job/posting",
        "location": [
            "City, State",
            "Remote"
        ],
        "active": true
    }

    //...possibly other contributions below
]
```
2) Click the pencil icon in the top right of the page to edit the file.
> Alternatively, you can manually [fork](https://github.com/pittcsc/Summer2024-Internships/fork) the repository and make your changes there.
3) To add a new internship, copy the example template, add it to the list at the bottom, and replace the values with the corresponding information. (Please make a new list entry for each unique position, even if they are for the same company.)

Here are more specifics about what each field means:

| Property Name   | Data Type        | Description                                          | Example |
| --------------- | ---------------- | ---------------------------------------------------- | -------- |
| **company_name**| `str`            | Name of company                                      | Google |
| **title**       | `str`            | Name of internship position                          | Machine Learning Software Engineer |
| **start_date**  | `str`            | Start date of internship (format: MM/DD/YYYY)        | 06/15/2024 |
| **url**         | `str`            | Link to job posting (include "https://")             | https://google.com/link/to/job/posting |
| **location**    | `[str]`          | Array of locations available for internship | ["Mountain View, CA", "Remote"] |
| **active**      | `bool`           | `true` if application is open. `false` if not.         | true |

4) Once you are done, the file should look something like this (there may be more than just two submissions in the file):

```jsonc
[
    {
        "company_name": "ExampleCompany",
        "title": "Software Engineering Internship Example",
        "start_date": "MM/DD/YYYY",
        "url": "https://example.com/this/is/a/link/to/the/job/posting",
        "location": [
            "City, State",
            "Remote"
        ],
        "active": true
    },

    //...other submissions (if any)

    {
        // your submission here
    }, 
]
```

5) Click `Commit changes...` in the top right of the page.
6) Select "*Create a new branch for this commit and start a pull request*" and click `Propose Changes`.
7) Finally, create a pull request to merge your changes.
8) That's it! Your contribution will be automatically added to the correct `README.md` once it is reviewed.

## Editing an Internship
To edit an internship (changing links, setting as inactive, changing start date, etc.), follow these steps:
1) Navigate to the file `listings.json`.
2) Click the pencil icon in the top right of the page to edit the file.
> Alternatively, you can manually [fork](https://github.com/pittcsc/Summer2024-Internships/fork) the repository and make your changes there.
3) Find the internship's entry in `listings.json` and edit the field(s) that you wish to update.
> Please do not change the `id` or `source` fields
4) Change the `updated_date` field to the current date.
5) Click `Commit changes...` in the top right of the page.
6) Select "*Create a new branch for this commit and start a pull request*" and click `Propose Changes`.
7) Finally, create a pull request to merge your changes.

## Deleting an Internship
It is preferable to set an internship as inactive (see [Editing an Internship](#Editing-an-Internship) above) rather than deleting it.

However, if there is a specific reason why you believe an internship should be removed from this repository entirely, please remove it from `listings.json` by creating a pull-request and specify why it should be deleted.

## Automatic README.md Updates
A script will automatically add new contributions as well as new internships found by [Simplify](https://simplify.jobs) to the appropriate README. The row will look something like this:
```md
| Company | Role | Location | Link | Status |
| --- | --- | --- | :---: | :---: |
| **[Example Company](https://link.to/company)** | Software Engineering Internship Example | San Francisco, CA | <img src="https://i.imgur.com/5JF7mJI.png" width="150" alt="Apply"> | ✅ |
```

When rendered, it will look like:
| Company | Role | Location | Link | Status |
| --- | --- | --- | :---: | :---: |
| **[Example Company]()** | Software Engineering Internship Example | San Francisco, CA | <img src="https://i.imgur.com/5JF7mJI.png" width="150" alt="Apply"> | ✅ |


