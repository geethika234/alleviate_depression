import json
import requests
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# list of email_id to send the mail
def group(li,mess,Subject):

	for i in range(len(li)):
		s = smtplib.SMTP("smtp.gmail.com:587")
		s.starttls()
		s.login("alleviatedep@gmail.com", "password")
		message = mess
		Mail_Body = MIMEMultipart()
		Mail_Body['Subject'] = Subject
		Mail_Msg = MIMEText(message)
		Mail_Body.attach(Mail_Msg)
		s.sendmail("roomserver.cds@gmail.com", li[i], Mail_Body.as_string())
		s.quit()

