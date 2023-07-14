import smtplib, ssl


def send_email(message):
    #global host, port, username, password, context, message, server
    host = "smtp.gmail.com"
    port = 465
    username = "shopping5501@gmail.com"
    password = "eofsdodycoufnhck"
    receiver = "shopping5501@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)