import smtplib
import config_pass


def send_mail(from_email, to_email, msg):
    username = config_pass.config_username
    password = config_pass.config_password
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_email, msg)
    server.quit()
