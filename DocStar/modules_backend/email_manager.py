import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(receiver_address, subject, mail_content):
    # The mail addresses and password
    sender_address = 'sda.doc.star@gmail.com'
    sender_pass = 'mycttvbzzlqweezz'

    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = subject

    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


if __name__ == "__main__":
    email = 'asimorawska@gmail.com'
    subject = 'test'
    user_text = 'test_pass'
    send_email(email, subject, user_text)
    # send_email(email, subject, user_text)
