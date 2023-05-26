import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
import pandas as pd

#Load environment variables
load_dotenv()

# SMTP server configuration
#smtp_server = "smtp-mail.outlook.com"
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv("smtp_username")
smtp_password = os.getenv("smtp_password")
#Email configuration
sender_email = os.getenv("sender_email")
subject = "Propuesta de automatización"
message = """

Estimado [Nombre_del_destinatario],

Saludos cordiales,

XXX


"""

# Load the Excel file
excel_file = os.getenv("excel_file")
sheet_name = os.getenv("sheet_name")
df = pd.read_excel(excel_file,sheet_name=sheet_name)


# Create a SMTP session
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Enable secure connection
    server.login(smtp_username, smtp_password)  # Login to the SMTP server
# Iterate over the rows
    for index, row in df.iterrows():
        
        name = row['Nombre']
        email = row['Email']
        if email != 'Email not available':
            message = message.replace(name,"[Nombre_del_destinatario]")
            # Email configuration
            receiver_email = email
            # Create a multipart message object
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            # Attach the message to the email
            msg.attach(MIMEText(message, 'plain'))
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
            
    







