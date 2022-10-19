# Contributing to the Internship List
Thank you for your interest in contributing to the Pitt CSC internship list! 

Below, you'll find the guidelines for our repository. Chances are, you can probably just look at how other internships are formatted and follow it. If you have any questions, please create an [issue](https://github.com/pittcsc/Summer2023-Internships/issues/new) here.

Finally, while these are guidelines, **don't** stress about making your submission perfect! If needed, we will fix your submission. Just try your best to follow the guidelines.

## Finding an Internship to Add
We ask that the internships that you add meet some requirements. Specifically, your internship must
- be in one of the following categories: 
    - software/computer engineering,
    - computer/data science,
    - product manager,
    - quant, and
    - any other tech-related internships.
- be for **summer 2023**. We will *not* accept internships for a different term.
- be located in the United States, Canada, or remote.
- not already exist in the internship list, and must not be pending review [here](https://github.com/pittcsc/Summer2023-Internships/pulls). 

Make sure to have the following information ready:
- The name of the position.
- The location of the position.
- A link to the job *description* page.The link should direct the user to the page, **not** a third party website or general careers page.
- The immigration requirements of the position
    - An easy way to check is to search for keywords like `visa` or `sponsorship`.

## Adding an Internship
Cool! You're ready to add an internship to the list.

First, be sure to [fork](https://github.com/pittcsc/Summer2023-Internships/fork) (see [this guide](https://docs.github.com/en/get-started/quickstart/fork-a-repo) for more information) the repository. This is how you will be able to make your changes.

Each row in the internship table is for a **company**. In other words, each row should correspond to a unique company. A row might look like this:
```md
| Company Name | Location of Position | Position Description |
```

### If the Company Doesn't Exist
Depending on the number of internships you plan on adding, what you're essentially adding might look a little different.
- adding **one** internship for a company:
    ```md
    | [Company's Name](Link to Job Post) | Location(s) | Name of Position |
    ```

    <details>
    <summary>Examples</summary>
    <br> 

    In Markdown, this might look like one of the following rows:

    ```md
    | [Target](https://jobs.target.com/job/-/-/1118/34525104848) | Brooklyn Park, MN | Software Engineering Intern - Hybrid (Starting June 2023) |
    | [ByteDance](https://jobs.bytedance.com/en/position/7138261141784611103/detail?spread=BSPP2KS) | Mountain View, CA | Software Engineer Intern |
    | [SpaceX](https://boards.greenhouse.io/spacex/jobs/6366187002?gh_jid=6366187002) | Multiple| 2023 Summer Intern - Software Engineer (US Citizens Only) | 
    ```

    When rendered, it will look like:

    | Name | Location |  Notes |
    | ---- | -------- | ------ |
    | [Target](https://jobs.target.com/job/-/-/1118/34525104848) | Brooklyn Park, MN | Software Engineering Intern - Hybrid (Starting June 2023) |
    | [ByteDance](https://jobs.bytedance.com/en/position/7138261141784611103/detail?spread=BSPP2KS) | Mountain View, CA | Software Engineer Intern |
    | [SpaceX](https://boards.greenhouse.io/spacex/jobs/6366187002?gh_jid=6366187002) | Multiple| 2023 Summer Intern - Software Engineer (US Citizens Only) | 
    
    </details>

- adding multiple **unique** internships for a company (e.g., the company has a SWE and PM internship):
    ```md
    | Company's Name | Location(s) | [Name of Position 1](Link1), [Name of Position 2](Link2), ..., [Name of Position N](LinkN) |
    ```

    <details>
    <summary>Examples</summary>
    <br> 

    In Markdown, this might look like one of the following rows:

    ```md
    | Adobe | Various | [Software Engineer Intern](https://careers.adobe.com/us/en/job/R131626/2023-Intern-Software-Engineer), [Software Engineer (Mobile Development) Intern](https://careers.adobe.com/us/en/job/R131674/2023-Intern-Software-Engineer-Mobile-Development) |
    | Delta | Atlanta, GA, Minneapolis St. Paul, MN | [Software Engineer Intern](https://delta.avature.net/careers/JobDetail/Intern-Software-Engineering-Summer-2023/17376), [Data Science Intern](https://delta.avature.net/careers/JobDetail/Intern-IT-Operations-Research-Data-Science-Summer-2023/17381), [Data Analytics Intern](https://delta.avature.net/careers/JobDetail/Intern-Revenue-Technology-Data-Analytics-Summer-2023/17650) |
    | Raytheon | Varies by Role | [UP 2023 Software Engineer Internships](https://careers.rtx.com/global/en/job/RAYTGLOBAL01567022EXTERNALENGLOBAL/UP-2023-Software-Engineer-Internships), [2023 Software Engineer Summer Intern](https://careers.rtx.com/global/en/job/RAYTGLOBAL01569607EXTERNALENGLOBAL/2023-Software-Engineer-Summer-Intern) (US Citizenship Required for Both) |
    ```

    When rendered, it will look like:

    | Name | Location |  Notes |
    | ---- | -------- | ------ |
    | Adobe | Various | [Software Engineer Intern](https://careers.adobe.com/us/en/job/R131626/2023-Intern-Software-Engineer), [Software Engineer (Mobile Development) Intern](https://careers.adobe.com/us/en/job/R131674/2023-Intern-Software-Engineer-Mobile-Development) |
    | Delta | Atlanta, GA, Minneapolis St. Paul, MN | [Software Engineer Intern](https://delta.avature.net/careers/JobDetail/Intern-Software-Engineering-Summer-2023/17376), [Data Science Intern](https://delta.avature.net/careers/JobDetail/Intern-IT-Operations-Research-Data-Science-Summer-2023/17381), [Data Analytics Intern](https://delta.avature.net/careers/JobDetail/Intern-Revenue-Technology-Data-Analytics-Summer-2023/17650) |
    | Raytheon | Varies by Role | [UP 2023 Software Engineer Internships](https://careers.rtx.com/global/en/job/RAYTGLOBAL01567022EXTERNALENGLOBAL/UP-2023-Software-Engineer-Internships), [2023 Software Engineer Summer Intern](https://careers.rtx.com/global/en/job/RAYTGLOBAL01569607EXTERNALENGLOBAL/2023-Software-Engineer-Summer-Intern) (US Citizenship Required for Both) |

    </details>

- adding multiple internships that are essentially the same for a company (e.g., the company has 4 SWE internships, with each of them only differing by location), you have two options:

    - If they have a reasonable number of locations, put:
        ```md
        | Company's Name | Multiple | Position Name @ [Location 1](Link1), [Location 2](Link2), ..., [Location N](Link N) |
        ```

        <details>
        <summary>Examples</summary>
        <br> 

        In Markdown, this might look like one of the following rows:

        ```md
        | [Garmin](https://careers.garmin.com/careers-home/jobs?tags3=Intern&page=1) | Various | Software Engineer Intern (Summer 2023): [Tulsa, OK](https://careers.garmin.com/careers-home/jobs/9345?lang=en-us), [Scottsdale, AZ](https://careers.garmin.com/careers-home/jobs/9267?lang=en-us), [Chandler, AZ](https://careers.garmin.com/careers-home/jobs/9266?lang=en-us), [Boulder, CO](https://careers.garmin.com/careers-home/jobs/9220?lang=en-us), [Tucson, AZ](https://careers.garmin.com/careers-home/jobs/9219?lang=en-us), [Cary, NC](https://careers.garmin.com/careers-home/jobs/9243?lang=en-us) |
        ```

        When rendered, it will look like:
        | Name | Location |  Notes |
        | ---- | -------- | ------ |
        | [Garmin](https://careers.garmin.com/careers-home/jobs?tags3=Intern&page=1) | Various | Software Engineer Intern (Summer 2023): [Tulsa, OK](https://careers.garmin.com/careers-home/jobs/9345?lang=en-us), [Scottsdale, AZ](https://careers.garmin.com/careers-home/jobs/9267?lang=en-us), [Chandler, AZ](https://careers.garmin.com/careers-home/jobs/9266?lang=en-us), [Boulder, CO](https://careers.garmin.com/careers-home/jobs/9220?lang=en-us), [Tucson, AZ](https://careers.garmin.com/careers-home/jobs/9219?lang=en-us), [Cary, NC](https://careers.garmin.com/careers-home/jobs/9243?lang=en-us) |

        </details>

    - If they have a *lot* of locations, *and* you provide a link to the job search page, put:
        ```md
        | [Company's Name](Link to Job Search Page) | Multiple | Position Name |
        ```
        Be sure to provide instructions on what the person has to do to get to the relevant postings via the description. **Note:** If your link to the job search page makes it easy to see all relevant internship positions, then providing a description isn't necessary.

        <details>
        <summary>Examples</summary>
        <br> 

        In Markdown, this might look like one of the following rows:

        ```md
        | [Northrop Grumman](https://ngc.wd1.myworkdayjobs.com/en-US/Northrop_Grumman_External_Site/details/College-Intern-Administrative---Documentation_R10064554-1?q=software%20engineer&workerSubType=a111b0a898f10129e4db58f2e700d97a) | Various | Software Engineer Intern (US Citizenship Required) |
        | [Keysight Technologies](https://jobs.keysight.com/go/Students/3065700/?q=&q2=&alertId=&title=software&location=US&shifttype=intern&department=)| Santa Rosa, CA | Various Positions |
        ```

        When rendered, it will look like:
        | Name | Location |  Notes |
        | ---- | -------- | ------ |
        | [Northrop Grumman](https://ngc.wd1.myworkdayjobs.com/en-US/Northrop_Grumman_External_Site/details/College-Intern-Administrative---Documentation_R10064554-1?q=software%20engineer&workerSubType=a111b0a898f10129e4db58f2e700d97a) | Various | Software Engineer Intern (US Citizenship Required) |
        | [Keysight Technologies](https://jobs.keysight.com/go/Students/3065700/?q=&q2=&alertId=&title=software&location=US&shifttype=intern&department=)| Santa Rosa, CA | Various Positions |

        </details>

If you have internships for multiple companies, repeat the process above. 

Once you have the rows, append them to the *bottom* of the table. So, for example, if you want to add the rows
```
| A | A | A |
| B | B | B |
```
and the table in the README currently has
```
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 | 
| 4 | 4 | 4 |

<!-- Please leave a one line gap between this and the table -->
...
```
add the rows like so:
```
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 | 
| 4 | 4 | 4 |
| A | A | A |
| B | B | B |

<!-- Please leave a one line gap between this and the table -->
```

### If the Company *Does* Exist
If the company already exists in the table, make sure the internship you're trying to add isn't already there!

If it isn't, then simply edit the existing row based on the specifications described above (under "If the Company Doesn't Exist"). **Do not move the row to the bottom of the internship list.** 

For example, if the README table looks like
```
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 3 | 
| 4 | 4 | 4 |

<!-- Please leave a one line gap between this and the table -->
...
```
and you wanted to edit the second row (the one with the `2`'s) to say `| B | B | B |`, then you would end up with:
```
| 1 | 1 | 1 |
| B | B | B |
| 3 | 3 | 3 | 
| 4 | 4 | 4 |

<!-- Please leave a one line gap between this and the table -->
...
```

## Removing an Internship
Suppose you come across an outdated entry or the posting is now closed. 

- If a company only has one internship offering, change the posting's formatting to:
    ```md
    | Company's Name | Location | **🔒 Closed 🔒** Name of Position |
    ```

    In other words, remove the link to the application page and put `**🔒 Closed 🔒**` before the description.

    <details>
    <summary>Examples</summary>
    <br> 

    Suppose that the Target closed their internship. Initially, the row might look like this:

    ```md
    | [Target](https://jobs.target.com/job/-/-/1118/34525104848) | Brooklyn Park, MN | Software Engineering Intern - Hybrid (Starting June 2023) |
    ```

    When rendered, it will look like:

    | Name | Location |  Notes |
    | ---- | -------- | ------ |
    | [Target](https://jobs.target.com/job/-/-/1118/34525104848) | Brooklyn Park, MN | Software Engineering Intern - Hybrid (Starting June 2023) |

    After you indicate that it's closed, the row should look like:

    ```md
    | Target | Brooklyn Park, MN | **🔒 Closed 🔒** Software Engineering Intern - Hybrid (Starting June 2023) |
    ```

    When rendered, it will look like:

    | Name | Location |  Notes |
    | ---- | -------- | ------ |
    | Target | Brooklyn Park, MN | **🔒 Closed 🔒** Software Engineering Intern - Hybrid (Starting June 2023) |

    </details>

- If the company has multiple **unique** internship offerings, then just remove *that* specific internship completely. If needed, update the relevant location. Be sure to follow the specifications for under "If the Company Doesn't Exist" when removing an internship.

## Editing an Internship
There aren't any specific guidelines here. As long as it is consistent with what we have above, then it should be fine.

## Done with Changes?
Once you're done with your changes, please create a **pull request** (for more information, click [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)). We will review your pull request and suggest changes if necessary. 
