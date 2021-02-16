import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = 'langw1460@gmail.com'#change and obfuscate later
password = 'lol1234xd'#change and obfuscate later
def send_appreciation_email(email:str):
    if '@' not in email:
        raise Exception
    s = []
    for x in list(email):
        if x == '@':
            break
        else:
            s.append(x)
    sss = "".join(s)
    message = MIMEMultipart('alternative')
    message["Subject"] = "Ignore me"
    message["From"] = sender_email
    message["To"] = email
    text = f"""\
    Test lang to @{sss} para makita ko kung nagana na
    """
    
    p = MIMEText(text, "plain")
    
    message.attach(p)
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as serv:
        serv.login(sender_email,password)
        serv.sendmail(sender_email,email,message.as_string())
        serv.close()
def send_mail(message:str,email:str):
    text = f"""\
    The sender({email}) said that: {message}
    """     
    message = MIMEMultipart('alternative')
    message["Subject"] = "Ignore me"
    message["From"] = sender_email
    message["To"] = email

    p = MIMEText(text, "plain")
    
    message.attach(p)
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as serv:
        serv.login(sender_email,password)
        serv.sendmail(sender_email,email,message.as_string())
        serv.close()
