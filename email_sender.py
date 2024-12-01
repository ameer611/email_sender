import smtplib

email = input('Enter the email of recipient: -> ')
content = input('Enter the content of mail: -> ')

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sender_email@gmail.com', 'sender password')
    server.send('sender_email@gmail.com', to, content)
    server.close()

send_email(email, content)