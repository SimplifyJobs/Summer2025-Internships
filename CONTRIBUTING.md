# Contributing to the Internship List
Thank you for your interest in contributing to the Pitt CSC internship list!

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

Open **contributions.json** and add a list item there with the information about the position. Please make a unique list entry for each unique position even if they are for the same company.

All new contributions will go to this file before being automatically added to the appropriate markdown file. In this JSON file there will be at least one list item which shows an example of what a new contribution will look like. The file will look something like this:
```json
[
    {
        "company_name": "ExampleCompany",
        "company_bio": "This is a short description of the company and what they do.",
        "title": "Software Engineering Internship Example",
        "start_date": "MM/DD/YYYY",
        "url": "example.com/this/is/a/link/to/the/job/posting",
        "location": [
            "City 1, State",
            "Location 2",
            "Remote"
        ],
        "active": true,
        "source": "Contribution"
    }
]
```

To add a new internship, simply copy the example template, add it to the list at the bottom and fill in all the corresponding information. Here are more specifics about what each property should entail:
- company_name: str = name of company
- company_bio: str = short description of company, what they do, what they stand for, or whatever feels right
- title: str = name of internship position
- start_date: str = start date of internship (please follow the date format so my script doesn't crash)
- url: str = link to job posting
- location: [str] = Array of locations available for internship. If just one, only add one list item. If remote option, include here.
- active: bool = true (false if no longer accepting applications)
- source: str = "Contribution" (Don't change)

When you are done, the file should look something like this:
```json
[
    {
        ...example object
    },
    {
        "company_name": "New Internship Company",
        "company_bio": "This is a short description of the company and what they do.",
        "title": "Job Title",
        "start_date": "05/1/2024",
        "url": "company.com/internship",
        "location": [
            "San Francisco, CA"
        ],
        "active": true,
        "source": "Contribution"
    }
]
```

We have a script that runs once daily, which will automatically add your contribution to the appropriate page in a row that looks something like this:
```md
| Company | Bio | Location | Role | Link | Status |
| --- | --- | --- | --- | --- | --- |
| [ExampleCompany](link to company page) | This is a short description of the company and what they do. | Location | Software Engineering Internship Example | [Job Posting](link to job posting page) | ✅ |
```

When rendered, it will look like:

| Company | Bio | Location | Role | Link | Status |
| --- | --- | --- | --- | --- | --- |
| [ExampleCompany]() | This is a short description of the company and what they do. | Location | Software Engineering Internship Example | [Job Posting]() | ✅ |


## Editing an Internship
To edit an internship (changing links, setting as inactive, changing start date, etc.), first, find the corresponding internship's entry in listings.json. Then pretend you are adding it as a new internship and follow the instructions above. Copy and paste the corresponding fields and change whichever ones need to be changed. Please only include the fields specified in the Adding an Internship section **plus the id field**. This is how we will make sure your edits replace the only internship.

## Done with Changes?
Once you're done with your changes, please create a **pull request** (for more information, click [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)). We will review your pull request and suggest changes if necessary.
