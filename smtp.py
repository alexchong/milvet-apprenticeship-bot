import smtplib
import ssl
# from getpass import getpass
from email.mime.text import MIMEText

context = ssl.create_default_context()  # SSL context
port = 465  # SMTPS port
server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)

receiver = ''
sender = '' # Gmail account must have Less Secured App access enabled
sender_password = ''

message = '''\
Subject: Auto-Notification: New Apprenticeships Available


Looks like there's new availability for the following positions:
'''

# initial login promopt for email access
def login():
    count = 0
    while (count < 3):
        try:
            # password = getpass('Enter sending Gmail password: ') # masked password input
            return server.login(sender, sender_password)
        except smtplib.SMTPAuthenticationError:
            count += 1
            print("Invalid password.\n")
        except smtplib.SMTPException as e:
            print(e)
        finally:
            if count == 3:
                exit()

def send():
  server.sendmail(sender, receiver, message)
  server.quit()