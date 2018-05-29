from email.header    import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email import encoders
from smtplib import SMTP_SSL, SMTP
import ntpath
from logs import Logs


class SendEmail():

    def __init__(self, mail):
        self.mail_to = mail['to']
        self.mail_from = mail['from']
        self.smtp_server = mail['smtp_server']
    
    def sendMessage(self, fpath, folder):
        try:
            fname = ntpath.basename(fpath)

            Logs.Print("Sending email for " + folder + " and file:    " + str(fname))

            msg = MIMEMultipart()
            msg['Subject'] = "ALARM DETECTED ON " + folder
            msg['From'] = "ALERT! " + "<" + self.mail_from + ">"
            msg['To'] = self.mail_to

            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(fpath, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="' + fname + '"')
            msg.attach(part)

            server = SMTP(self.smtp_server, timeout=10)
            server.set_debuglevel(0)

            #server.login(self.username, self.password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            Logs.Print('Message sent')

        except Exception as e:
            Logs.Print("Exception: " + str(e))

        finally:
            if server:
                server.quit()

