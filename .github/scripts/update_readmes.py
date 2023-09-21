from datetime import datetime
import util


def main():

    listings = util.getListingsFromJSON()

    util.checkSchema(listings)
    util.sortListings(listings)

    summer_2024_listings = util.filterSummer(listings)
    util.embedTable(summer_2024_listings, "README.md")

    offseason_listings = util.filterOffSeason(listings)
    util.embedTable(offseason_listings, "README-Off-Season.md", offSeason=True)

    util.setOutput("commit_message", "Updating READMEs at " + datetime.now().strftime("%B %d, %Y %H:%M:%S"))


if __name__ == "__main__":
    main()
