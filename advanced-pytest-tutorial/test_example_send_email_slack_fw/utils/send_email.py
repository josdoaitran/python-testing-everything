import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(name)s-%(levelname)s-%(message)s')

class EmailUtils:
    def send_email(subject, email_content):
        sender_email = os.environ.get("sender.email")
        recipient_email = os.environ.get("receiver.email")
        app_password = os.environ.get("sender.password")

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        body = email_content
        msg.attach(MIMEText(body, 'plain'))

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, app_password)

            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            logger.info("Email sent successfully!")

        except Exception as e:
            logger.error(f"Failed to send email: {e}")

        finally:
            server.quit()