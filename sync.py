import gspread
import markdown2
from bs4 import BeautifulSoup

GOOGLE_CREDENTIALS_FILE = './gcred.json'

def parse_markdown_to_html_table():
    """ Parse README.md, convert to HTML, return table """
    readme = open("README.md", 'r').read()
    html = markdown2.markdown(readme, extras=['tables'])
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table")
    return table

def parse_html_table(table):
    """ Parse HTML table into proper formatted array that can be written to Google Sheet."""
    result = []
    rows = table.findAll('tr')
    for row in rows:
        current_row = []
        cols = row.findAll(['td', 'th'])
        for cell in cols:
            current_row.append(html_to_spreadsheet_cell(cell))
        result.append(current_row)
    filler_rows = [["", "", "", ""] for x in range(10)]
    return result + filler_rows

def html_to_spreadsheet_cell(html_element):
    """ Parse HTML element, like <a href=www.google.com>Google</a> to =HYPERLINK(www.google.com, Google) """
    link = html_element.find("a")
    if link:
        return '=HYPERLINK("{}", "{}")'.format(link['href'], link.contents[0])
    else:
        return html_element.text

html = parse_markdown_to_html_table()
parsed_sheet_data = parse_html_table(html)

print("Connecting to Google Sheet...")
gc = gspread.service_account(filename=GOOGLE_CREDENTIALS_FILE)

sh = gc.open_by_key('1bJq7YQV19TWyzPCBeQi5P4uOm8uiAAm2AHCnVNGRIDg')
sheet = sh.get_worksheet(0)

sheet.update('A7', parsed_sheet_data, raw=False)




