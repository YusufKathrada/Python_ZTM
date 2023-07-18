import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Yusuf Kathrada'

# Enter email address you wish to send to
email['to'] = '<to email address>

# Enter message you wish to send
email['subject'] = '<type message you wish to send>'

email.set_content(html.substitute({'name': '<name of person you sending to>'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()

  # Enter your email details
  smtp.login('<your email address>', '<your password>')
  smtp.send_message(email)
  print('all good boss!')
