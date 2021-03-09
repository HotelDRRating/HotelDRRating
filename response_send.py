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
def send_register(email,fullname,hash):
    if '@' not in email:
        raise ValueError("Please make sure your email address is a valid email address")
    s = []
    for x in list(email):
        if x == '@':
            break
        else:
            s.append(x)
    sss = "".join(s)
    message = MIMEMultipart('alternative')
    message["Subject"] = "Thank you for registering"
    message["From"] = sender_email
    message["To"] = email
    msg = MIMEText(f"""
        <!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css" integrity="sha512-+4zCK9k+qNFUR5X+cKL9EIR+ZOhtIloNl9GIKS57V1MyNsYpYcUrUeQc9vNfzsWfV28IaLL3i96P9sdNyeRssA==" crossorigin="anonymous" />
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    
    </head>
    <body style="background-image: url('http://www.hoteldrrating.com/resources/images/full-body-bg2.jpg');width:1920px;height:1080px;">
        <div class="container-fluid">
            <h1 class="display-4">Thank you {fullname} for registering</h1>
            <div class="row">
                <p display="3">Click <a href="https://localhost:5000/verify?hash={hash}">Here</a> to verify your account</p>
            </div>
        </div>
        <div class='row display-2'>
            Regards, Disaster Resistance for Hotel Rating.
        </div>
    </body>
</html>
                    """, 'html', 'utf-8')
    
    message.attach(msg)
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as serv:
        serv.login(sender_email,password)
        serv.sendmail(sender_email,email,message.as_string())
        serv.close()
send_register("walalang985@gmail.com","TEST TEST","TESTHASH")