{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw12240\paperh20160\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import smtplib\
from email.mime.text import MIMEText\
from email.mime.multipart import MIMEMultipart\
from dotenv import load_dotenv\
import os\
\
load_dotenv()  # Load .env file variables\
\
def send_failure_email(error_message):\
    sender_email = os.getenv("EMAIL_USER")\
    receiver_email = os.getenv("EMAIL_TO")\
    email_password = os.getenv("EMAIL_PASS")\
\
    subject = "ETL Process Failed"\
    body = f"ETL process failed with the following error:\\n\\n\{error_message\}"\
\
    msg = MIMEMultipart()\
    msg['From'] = sender_email\
    msg['To'] = receiver_email\
    msg['Subject'] = subject\
    msg.attach(MIMEText(body, 'plain'))\
\
    try:\
        with smtplib.SMTP('smtp.gmail.com', 587) as server:\
            server.starttls()\
            server.login(sender_email, email_password)\
            server.send_message(msg)\
            print("Failure email sent successfully.")\
    except Exception as e:\
        print("Error sending failure email:", e)\
\
}