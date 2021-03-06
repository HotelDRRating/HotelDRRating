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
def send_register(email,otp):
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
    msg = MIMEText("""
        <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        </head>
        <body>
        <a href="www.google.com">test</a>
        </body>
                    """, 'html', 'utf-8')
    
    message.attach(msg)
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as serv:
        serv.login(sender_email,password)
        serv.sendmail(sender_email,email,message.as_string())
        serv.close()
send_register("aacabanas2@student.apc.edu.ph",696969)