import pymysql as psql,smtplib,ssl,base64 as b64
from Crypto import Random
from Crypto.PublicKey import RSA
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class rsa(object):
    def __init__(self):
        return
    def generate_key(self,bits=2048):
        private = RSA.generate(bits,Random.new().read)
        public = private.publickey()
        return private.exportKey(),public.exportKey()
    def encrypt(self,string,pubkey):
        return b64.b64encode(pubkey.encrypt(string,32)[0]) 
class emailing(object):
    sender_email = 'V!6ga2$r6?Jf$8Ye¥oI1@73EG?o@kl7?yOp#¢5Bt$8YeB6$&a2$rr!0XV!6gp0t$Yo!fu$t!B6$&'#change and obfuscate later
    password = 'V!6gu$t!V!6g@73E8?Ty£tOyG?o@Pk&*q8u?'#change and obfuscate later
    def __init__(self):
        return
    def send_thank_you(self,email:str):
        if '@' not in email:
            raise ValueError
        s = []
        for q in list(email):
            if q == '@':
                break
            else:
                s.append(q)
        sender = "".join(s)
        message = MIMEMultipart('alternative')
        message["Subject"] = "Thank You"
        message["From"] = self.sender_email
        message["To"] = email
        msg = f"""\
            Thank you {sender} for reaching out to us our support team will get back to you within 24 hours

            Regards.
            The Disaster Resilience Rating For Hotels            
            """
        message.attach(MIMEText(msg,"plain"))

        with smtplib.SMTP_SSL('smtp.gmail.com',465, context = ssl.context()) as serv:
            serv.login(self.sender_email,self.password)
            serv.sendmail(self.sender_email,email,message.as_string())
            serv.close()
        

