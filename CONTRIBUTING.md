# Contributing to the Internship List
Thank you for your interest in contributing to the Pitt CSC and Simplify internship list!

Below, you'll find the guidelines for our repository. If you have any questions, please create an [issue](https://github.com/pittcsc/Summer2024-Internships/issues/new) here.

## Finding an Internship to Add
We ask that the internships that you add meet some requirements. Specifically, your internship must
- be in one of the following categories:
    - software/computer engineering,
    - computer/data science,
    - product manager,
    - quant, and
    - any other tech-related internships.
- be located in the United States, Canada, or remote.
- not already exist in the internship list, and must not be pending review [here](https://github.com/pittcsc/Summer2024-Internships/pulls).

Note that we have multiple READMEs for different internship terms:
- [Summer 2024 internships](https://github.com/pittcsc/Summer2024-Internships/blob/dev/README.md)
- [Summer 2023 internships](https://github.com/pittcsc/Summer2024-Internships/blob/dev/README-2023.md)
- [Off-season internships](https://github.com/pittcsc/Summer2024-Internships/blob/dev/README-Off-Season.md)

Make sure to have the following information ready:
- The name of the position.
- The company name and a short description
- The location of the position.
- The start date (can be approximate) of the position
- A link to the job *description* page. The link should direct the user to the page for the position itself, **not** a third-party website or general careers page.

## Adding an Internship
Cool! You're ready to add an internship to the list.

First, be sure to [fork](https://github.com/pittcsc/Summer2024-Internships/fork) (see [this guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo) for more information) the repository. This is how you will be able to make your changes.

Open `contributions.json` and add a list item there with the information about the position. Please make a unique list entry for each unique position even if they are for the same company.

All new contributions will go to this file before being automatically added to the appropriate markdown file. In this JSON file there will be at least one list item which shows an example of what a new contribution will look like. The file will look something like this:
```json
[
    {
        "company_name": "ExampleCompany",
        "title": "Software Engineering Internship Example",
        "start_date": "MM/DD/YYYY",
        "url": "example.com/this/is/a/link/to/the/job/posting",
        "location": [
            "City 1, State",
            "Remote"
        ],
        "active": true,
        "source": "Contribution"
    }
]
```

To add a new internship, copy the example template, add it to the list at the bottom, and fill in all the corresponding information. Here are more specifics about what each property means:

| Property Name   | Data Type        | Description                                          |
| --------------- | ---------------- | ---------------------------------------------------- |
| **company_name**| `str`            | Name of company                                      |
| **title**       | `str`            | Name of internship position                          |
| **start_date**  | `str`            | Start date of internship (format: DD/MM/YYYY)        |
| **url**         | `str`            | Link to job posting                                  |
| **location**    | `[str]`          | Array of locations available for internship (include "Remote" if there is remote option)          |
| **active**      | `bool`           | `true` (`false` if no longer accepting apps)         |
| **source**      | `str`            | "Contribution" (Don't change. 'Simplify' denotes internship added from Simplify's database)                        |

After adding your submission, the file should look something like this:
```json
[
    {
        "company_name": "ExampleCompany",
        "title": "Software Engineering Internship Example",
        "start_date": "MM/DD/YYYY",
        "url": "example.com/this/is/a/link/to/the/job/posting",
        "location": [
            "City 1, State",
            "Remote"
        ],
        "active": true,
        "source": "Contribution"
    },
    ...,
    {
        ...your submission
    }
]
```
Once you are finished, submit your internship(s) by creating a **pull-request** (See Below)

## Editing an Internship
To edit an internship (changing links, setting as inactive, changing start date, etc.), follow these steps:
1) Find the corresponding internship's entry in `listings.json`.
2) Pretend you are adding it as a new internship and follow the instructions above.
3) Copy and paste the corresponding fields from `listings.json` to `contributions.json` and change whichever ones need to be changed.
> Please only include the fields specified in the Adding an Internship section **AND the id field**. This is how we will make sure your edits replace the only internship.
4) Submit a pull request as detailed below.

## Done with Changes?
Once you're done with your changes, please create a **pull request** (for more information, click [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)). We will review your pull request and suggest changes if necessary.

## Adding to the Markdown Table
We have a script that will automatically add your contribution to the appropriate page in a row that looks something like this:
```md
| Company | Location | Role | Link | Status |
| --- | --- | --- | --- | --- |
| **[Example Company](link.to/company)** | San Francisco, CA | Software Engineering Internship Example | <a href="example.com/this/is/a/link/to/the/job/posting"><img src="https://i.imgur.com/iPfAI7z.png" width="300" alt="Apply"></a> | ✅ |
```

When rendered, it will look like:

| Company | Location | Role | Link | Status |
| --- | --- | --- | --- | --- |
| **[Example Company]()** | San Francisco, CA | Software Engineering Internship Example | <a href="example.com/this/is/a/link/to/the/job/posting"><img src="https://i.imgur.com/iPfAI7z.png" width="300" alt="Apply"></a> | ✅ |

