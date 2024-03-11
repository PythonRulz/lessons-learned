import os
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()

def compile_send_email():
    
    email_sender = 'mweaver2k@gmail.com'
    email_password = f"{os.getenv("MAIL_PASS")}"
    email_receiver = 'michael_weaver@outlook.com'

    subject = 'EOD Stock Results'
    body = 'Stifel Individual Investments'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    em.add_alternative(body, subtype='html')

    with open('index.html', 'rb') as attachment_file:
        file_data = attachment_file.read()
        file_name = attachment_file.name.split("/")[-1]

    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(file_data)
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", f'attachment; filename="{file_name}"')
    em.attach(attachment)                      

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

