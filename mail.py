import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sender_mail", "Password")

# message to be sent
message = "This mail is as your php/html webpage has some error so please check it......"

# sending the mail
s.sendmail("sender_mail", "receiver_mail", message)

# terminating the session
s.quit()
