## Credit to Haider Imtiaz

# Automate Emails with Python
import imaplib
import email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Read Email
Email = imaplib.IMAP4_SSL('imap.gmail.com')
Email.login('your_username', 'your_password')
status, msgs = Email.select('INBOX')    
print("Status: ", status)
for i in range(1, int(msgs[0])):
    res, message = Email.fetch(str(i), '(RFC822)')
    for r in message:
        if isinstance(r, tuple):
            message = email.message_from_bytes(r[1])
            print (message["subject"])
#---------------------------------------------------
# Send Email
Your_Email = "test@xyz.com" 
password = "your_password"
reciver = "Sender Mail" 
subject = "Medium Article"
text_msg = "Hi, Codedev010 here from Medium Article"
msg = MIMEMultipart()
msg["From"] = Your_Email
msg["To"] = reciver
msg["Subject"] = subject
msg.attach(MIMEText(text_msg, 'plain'))
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(Your_Email, password)
MSG = msg.as_string()
server.sendmail(Your_Email, reciver, MSG)
server.quit()

#---------------------------------------------------