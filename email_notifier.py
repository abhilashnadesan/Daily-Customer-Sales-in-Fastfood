import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import sys

# ✅ Load .env from full path (important for cron or Airflow)
dotenv_path = '/Users/jenniferabhilash/Desktop/EUBS/Third Semester/daily fastfood project/.env'  # ⬅️ CHANGE this to your actual path
load_dotenv(dotenv_path=dotenv_path)

def send_alert(subject, body):
    sender_email = os.getenv("EMAIL_USER")
    receiver_emails = os.getenv("EMAIL_TO", "").split(",")  # ✅ handles multiple recipients
    email_password = os.getenv("EMAIL_PASS")

    print(f"[INFO] From: {sender_email}")
    print(f"[INFO] To: {receiver_emails}")
    print(f"[INFO] Subject: {subject}")

    # ✅ Check for missing variables
    if not sender_email or not receiver_emails or not email_password:
        print("[ERROR] Missing email configuration in .env file.")
        return

    # Build the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(receiver_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, email_password)
            server.sendmail(sender_email, receiver_emails, msg.as_string())
        print("[INFO] Alert email sent successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to send email: {e}")

# ✅ Support running from command line
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 email_notifier.py 'Subject' 'Message'")
    else:
        subject = sys.argv[1]
        message = sys.argv[2]
        send_alert(subject, message)
