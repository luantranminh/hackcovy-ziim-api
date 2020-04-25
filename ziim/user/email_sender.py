import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv
load_dotenv()


#The mail addresses and password
sender_address = os.getenv('SENDER_EMAIL')
sender_pass = os.getenv('SENDER_PASSWORD')

def send_payment_success_email(receiver_address, code):
    try:
      os.chdir('ziim/templates')
      env = Environment(loader=FileSystemLoader(os.getcwd()))
      template = env.get_template('receive_code.html')
      html_content = template.render(code=code)


      message = MIMEMultipart()
      message['From'] = sender_address
      message['To'] = receiver_address
      message['Subject'] = 'Payment Successful'   
      message.attach(MIMEText(html_content, 'html'))

      session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
      session.starttls() #enable security
      session.login(sender_address, sender_pass) #login with mail_id and password
      text = message.as_string()
      session.sendmail(sender_address, receiver_address, text)
      session.quit()
      return "Email sent successfully"

    except Exception as e:
      return "Unable to Send Email"