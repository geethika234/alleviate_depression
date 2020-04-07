import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

  
# list of email_id to send the mail 
def group(li,mess,Subject):
  
	emailfrom = "alleviatedep@gmail.com"
        for i in range(len(li)):
                emailto =li[i]
                fileToSend = ["values.csv"]
                username = "alleviatedep@gmail.com"
                password = "password"
                #print(li[i])
                msg = MIMEMultipart()
                msg["From"] = username
                msg["To"] = emailto
                msg["Subject"] = Subject
                for k in fileToSend:
                        ctype, encoding = mimetypes.guess_type(k)
                        if ctype is None or encoding is not None:
                                ctype = "application/octet-stream"
                        maintype, subtype = ctype.split("/", 1)
                        if maintype == "text":
                                fp = open(k)
                                # Note: we should handle calculating the charset
                                attachment = MIMEText(fp.read(), _subtype=subtype)
                                fp.close()
                        elif maintype == "image":
                                fp = open(k, "rb")
                                attachment = MIMEImage(fp.read(), _subtype=subtype)
                                fp.close()
                        elif maintype == "audio":
                                fp = open(k, "rb")
                                attachment = MIMEAudio(fp.read(), _subtype=subtype)
                                fp.close()
                        else:
                                fp = open(k, "rb")
                                attachment = MIMEBase(maintype, subtype)
                                attachment.set_payload(fp.read())
                                fp.close()
                                encoders.encode_base64(attachment)
                        attachment.add_header("Content-Disposition", "attachment", filename=k)
                        msg.attach(attachment)
		Mail_Msg = MIMEText(mess)
		msg.attach(Mail_Msg)
                server = smtplib.SMTP("smtp.gmail.com:587")
                server.starttls()
                server.login(username,password)
                server.sendmail(emailfrom, emailto, msg.as_string())
                server.quit()

