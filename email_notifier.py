import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

def send_alert(subject, body):
    sender_email = os.getenv("EMAIL_USER")
    receiver_email = os.getenv("EMAIL_TO")
    email_password = os.getenv("EMAIL_PASS")

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.send_message(msg)
            print("Alert email sent successfully.")
    except Exception as e:
        print("Error sending alert email:", e)
