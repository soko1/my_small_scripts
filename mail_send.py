#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

#
# mailserver settings
#
fromaddr = "address@example.com"
smtp_login = "address"
smtp_passwd = "password"
smtp_address = "mail.example.com"
smtp_port = 25
toaddr = "sendto@example.com"

#
# letter settings
#
# name of file for attach
filename = "report.csv"
# path to file
filename_path = "/etc/hosts"
# body of the letter
body = "blablabla"
# subject 
subj = "Report"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subj

msg.attach(MIMEText(body, 'plain'))
 

attachment = open(filename_path, "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP(smtp_address, smtp_port)
server.starttls()
server.ehlo()
server.login(smtp_login, smtp_passwd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
