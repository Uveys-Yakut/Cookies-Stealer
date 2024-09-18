import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import logging

logging.basicConfig(filename="email_sender.log", level=logging.DEBUG, format='%(asctime)s: %(message)s', encoding='utf-8')

load_dotenv()

def send_email(subject, body, attachment_path):
    email_host = os.getenv('EMAIL_HOST')
    email_port = int(os.getenv('EMAIL_PORT'))
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password = os.getenv('EMAIL_PASSWORD')
    email_to = os.getenv('EMAIL_TO')
    
    try:
        msg = MIMEMultipart()
        msg['From'] = email_address
        msg['To'] = email_to
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with open(attachment_path, 'rb') as file:
            part = MIMEApplication(file.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)

        with smtplib.SMTP(email_host, email_port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.send_message(msg)
        
        logging.info(f"Email sent to {email_to} with attachment {attachment_path}")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")
