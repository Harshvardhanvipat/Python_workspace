import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'test user'
email['to'] = 'ddclash76@gmail.com'
email['subject'] = 'you will be a future wizard'

email.set_content('I am a Python Master')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ddclash76@gmail.com', 'here you enter your password')
    smtp.send_message(email)
    print('all good boss!')
