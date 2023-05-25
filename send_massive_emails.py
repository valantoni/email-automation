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

Espero que este correo electrónico encuentre a tu empresa en buen estado. Mi nombre es Antonio y represento a Valerapp, una empresa especializada en la automatización de procesos empresariales.

Me complace ponerme en contacto contigo para ofrecerte nuestros servicios de automatización de procesos, diseñados específicamente para ayudar a las empresas a mejorar su eficiencia, reducir costos y aumentar la productividad. Nuestro enfoque se basa en la implementación de soluciones tecnológicas personalizadas que optimizan y agilizan los procesos clave de tu negocio.

Algunos de los beneficios que podemos ofrecerte incluyen:

Ahorro de tiempo y recursos: Mediante la automatización de tareas repetitivas y tediosas, puedes liberar a tu equipo de trabajo de actividades manuales, permitiéndoles enfocarse en tareas de mayor valor y estratégicas.

Mejora de la precisión y calidad: Nuestras soluciones automatizadas minimizan los errores humanos, lo que garantiza una mayor precisión en los procesos y mejora la calidad de los resultados.

Aumento de la productividad: Al optimizar tus procesos, podrás realizar más en menos tiempo, lo que se traduce en una mayor productividad para tu empresa y una ventaja competitiva en el mercado.

Reducción de costos: La automatización de procesos puede ayudarte a reducir los gastos operativos al eliminar tareas innecesarias, minimizar los errores que generan costos adicionales y maximizar la utilización de los recursos disponibles.

Me encantaría tener la oportunidad de discutir cómo nuestras soluciones de automatización pueden adaptarse a las necesidades específicas de tu empresa y ayudarte a alcanzar tus objetivos. Estoy disponible para agendar una llamada o una reunión en la que podamos explorar en detalle cómo podemos mejorar tus procesos y obtener los resultados deseados.

Agradezco tu tiempo y consideración. No dudes en responder a este correo electrónico para cualquier consulta o para concertar una cita. Espero tener la oportunidad de colaborar contigo y contribuir al crecimiento de tu negocio.

Saludos cordiales,

Antonio


"""

# Load the Excel file
excel_file = os.getenv("excel_file")
sheet_name = os.getenv("sheet_name")
df = pd.read_excel(excel_file,sheet_name=sheet_name)


# Create a SMTP session
with smtplib.SMTP(smtp_server, smtp_port) as server:
# Iterate over the rows
    for index, row in df.iterrows():
        
        name = row['Nombre']
        email = row['Email']
        if email != 'Email not available':
            message = message.replace(name,"Nombre_del_destinatario")
            # Email configuration
            receiver_email = email
            # Create a multipart message object
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject

            # Attach the message to the email
            msg.attach(MIMEText(message, 'plain'))

            server.starttls()  # Enable secure connection
            server.login(smtp_username, smtp_password)  # Login to the SMTP server
            server.sendmail(sender_email, receiver_email, msg.as_string())  # Send the email
            print('Email sent successfully.')
    







