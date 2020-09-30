from datetime import datetime,date,timedelta
import gspread
import markdown2
from bs4 import BeautifulSoup
# import os

GOOGLE_CREDENTIALS_FILE = './gcred.json'
EMAIL_SHEET_ID = "1TxQ_LSjOokvNnxyjlUpewA9Iq7F7Uknv0a6mh8dOQOk"

def parse_markdown_to_html_table():
    """ Parse README.md, convert to HTML, return table """
    readme = open("README.md", 'r', encoding="utf8").read()
    html = markdown2.markdown(readme, extras=['tables'])
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table")
    return table

print("Connecting to Google Sheet...")
gc = gspread.service_account(filename=GOOGLE_CREDENTIALS_FILE)

sh = gc.open_by_key('1bJq7YQV19TWyzPCBeQi5P4uOm8uiAAm2AHCnVNGRIDg')
posting_sheet = sh.get_worksheet(0)

# parse the table from the google sheet
dates = posting_sheet.col_values(4)

today = date.today()
start_delta = timedelta(weeks=1)
last_week = today - start_delta

# figure out the ones in the table that have been added within the last week
posting_index = -1
for i, date in reversed(list(enumerate(dates))):
    if date == '':
        continue
    parsed_date = datetime.strptime(date, '%m/%d/%Y').date()
    
    if parsed_date < last_week:
        posting_index = i + 1
        break

if posting_index != len(dates):
    # email the list out to people
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    sh = gc.open_by_key(EMAIL_SHEET_ID)
    email_sheet = sh.get_worksheet(1)
    names = email_sheet.col_values(2)[1:]
    subscription_emails = email_sheet.col_values(3)[1:]

    unsubscribed = sh.get_worksheet(1).col_values(1)[1:]

    emails = list(set(subscription_emails) - set(unsubscribed))

    table = parse_markdown_to_html_table()
    latest_postings = table.find("tbody").find_all("tr")[posting_index - 7:]
    latest_postings = [str(posting) for posting in latest_postings]

    sender_email = "pittcsc.internships@gmail.com"
    receiver_emails = emails

    def get_password():
        pass_word = None
        with open("pass.txt") as reader: 
            pass_word = reader.read()
        return pass_word

    password = get_password()



    message = MIMEMultipart("alternative")
    message["Subject"] = f'{today} CSC Internship Newsletter' 
    message["From"] = sender_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,

    If you are seeing this, please open the email in HTML.

    Best,
    Pitt CSC

    Unsubscribe Link: https://forms.gle/b7c1Eh3geFMJwor87 
    """
    html = f"""\
    <html>
    <p> Hi,  <br><br>
    Here are this week's CSC internship postings. Good luck! <br> 
    </p>
    <body>
        <table style="border: 1px solid black" >
            <thead style="border: 1px solid black">
                <tr style="border: 1px solid black">
                    <th style="border: 1px solid black">Name</th>
                    <th style="border: 1px solid black">Location</th>
                    <th style="border: 1px solid black">Notes</th>
                </tr>
            </thead>
            <tbody style="border: 1px solid black">
                {' '.join(latest_postings)}
            </tbody>
        </table>
        <p> More job postings <a href="https://github.com/Pitt-CSC/Summer2021-Internships">here</a>! </p>
    </body>
    <p> Best, <br>Pitt CSC<br>
    <a href="https://pittcsc.org/">pittcsc.org</a>
    <br>
    <br>
    <br>
    <br>
    <a href="https://forms.gle/b7c1Eh3geFMJwor87">Unsubscribe Here</a>
    </p>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_emails, message.as_string()
        )
