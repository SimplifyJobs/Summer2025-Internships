import json
from datetime import datetime
import os
import util
import re


def main():

    listings = util.getListingsFromJSON()

    sponsorship_pattern = r'\(.*?sponsorship.*?\)'
    citizen_pattern = r'\(.*?citizen.*?\)'
    for listing in listings:
        orig_title = listing["title"]
        new_title = re.sub(sponsorship_pattern, '', listing["title"], flags=re.IGNORECASE)
        no_sponsorship = orig_title != new_title
        other = no_sponsorship and "f1" in orig_title.lower()
        orig_title2 = new_title
        new_title = re.sub(citizen_pattern, '', orig_title2, flags=re.IGNORECASE)
        citizenship = new_title != orig_title2
        listing["title"] = new_title
        if other:
            listing["sponsorship"] = "Other"
        elif no_sponsorship:
            listing["sponsorship"] = "Does Not Offer Sponsorship"
        elif citizenship:
            listing["sponsorship"] = "U.S. Citizenship is Required"
        else:
            listing["sponsorship"] = "Offers Sponsorship"

    with open(".github/scripts/listings.json", "w") as f:
        f.write(json.dumps(listings, indent=4))
    return
    

    util.checkSchema(listings)
    util.sortListings(listings)

    summer_2024_listings = util.filterSummer(listings)
    util.embedTable(summer_2024_listings, "README.md")

    offseason_listings = util.filterOffSeason(listings)
    util.embedTable(offseason_listings, "README-Off-Season.md", offSeason=True)

    util.setOutput("commit_message", "Updating READMEs at " + datetime.now().strftime("%B %d, %Y %H:%M:%S"))


if __name__ == "__main__":
    main()
