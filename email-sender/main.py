# importing stuff
import os
from dotenv import find_dotenv, load_dotenv
from email.message import EmailMessage
import ssl
import smtplib

# loading the password
load_dotenv(find_dotenv())
PASS = os.getenv("EMAIL_PASS")

# emial contents
email_sender = "tensaicoder@gmail.com"
email_reciever ="tadanotensai05@gmail.com" 
email_password = PASS
subject = "testing email automation"
body="""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras pellentesque lectus eget elit ultricies gravida.
"""

email = EmailMessage()
email['From'] = email_sender
email['To'] = email_reciever
email['Subject'] = subject
email.set_content(body)

# making the connection secure
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, [email_reciever], email.as_string())