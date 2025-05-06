# importing stuff
import os
from dotenv import find_dotenv, load_dotenv
from email.message import EmailMessage
import ssl
import smtplib
from yaspin import yaspin

# loading the password
load_dotenv(find_dotenv())
PASS = os.getenv("EMAIL_PASS")

# emial contents
email_sender = "tadanotensai05@gmail.com"
email_reciever ="geniusjoel2005@gmail.com" 
email_password = PASS or ""
subject = input("Subject: ")
print("Body: (ctrl-d)")
content=[]
while True:
    try:
        line=input()
    except EOFError:
        break
    content.append(line)
body="\n".join(content)

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_reciever
email['Subject'] = subject
email.set_content(body)

# making the connection secure
context = ssl.create_default_context()

with yaspin(text="Sending...") as spinner:
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, [email_reciever], email.as_string())
        spinner.ok("󰩐")
        print("Mail sent successfully")
    except Exception:
        spinner.fail("⤬")
