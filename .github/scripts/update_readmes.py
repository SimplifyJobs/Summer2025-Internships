from datetime import datetime
import util


def main():

    listings = util.getListingsFromJSON()

    util.checkSchema(listings)
    util.sortListings(listings)

    summer_2025_listings = util.filterSummer(listings, "2025", earliest_date=1710797957)
    util.embedTable(summer_2025_listings, "README.md")

    offseason_listings = util.filterOffSeason(listings)
    util.embedTable(offseason_listings, "README-Off-Season.md", offSeason=True)

    util.setOutput("commit_message", "Updating READMEs at " + datetime.now().strftime("%B %d, %Y %H:%M:%S"))


if __name__ == "__main__":
    main()
