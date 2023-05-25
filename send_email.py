import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()

# Email configuration
sender_email = 'Test@hotmail.com'
receiver_email = 'contacto@gmail.com'
subject = 'Subject of the Email'
message = 'This is the body of the email.'

# Create a multipart message object
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Attach the message to the email
msg.attach(MIMEText(message, 'plain'))

# SMTP server configuration
smtp_server = 'smtp.gmail.com'
#smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
smtp_username = os.getenv('smtp_username')
smtp_password = os.getenv('smtp_password')

# Create a SMTP session
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  
    server.login(smtp_username, smtp_password)  
    server.sendmail(sender_email, receiver_email, msg.as_string()) 
    print('Email sent successfully.')
