import smtplib,ssl,random as rand,string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender_email = 'langw1460@gmail.com'#change and obfuscate later
password = 'lol1234xd'#change and obfuscate later
ctr = 1
while True:
    rands = rand.randint(0,9999999)
    message = MIMEMultipart('alternative')
    message["Subject"] = ''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    message["From"] = sender_email
    message["To"] = 'walang985@gmail.com'
    text = f"""\
    {rands}
    """
    
    p = MIMEText(text, "plain")
    
    message.attach(p)
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as serv:
        serv.login(sender_email,password)
        serv.sendmail(sender_email,'walang985@gmail.com',message.as_string())
        serv.close()    
    print(f"sent {ctr} emails")
    ctr +=1