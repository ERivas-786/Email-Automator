import smtplib
import ssl
from email.message import EmailMessage


# Enter the email address you wish to send the email from
email_sender = 'ENTER YOUR EMAIL'
# Enter your generated app password
email_password = 'ENTER YOUR PASSWORD'

my_file = open("emails.txt", "r")

# data reads the information in the emails.txt file
data = my_file.read()

email_receivers = data.split("\n")
print(email_receivers)
my_file.close()

# THESE ARE THE FIELDS WHERE THE SUBJECT AND YOUR EMAIL BODY ARE ENTERED
subject = 'ENTER SUBJECT HERE'
body = """
   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""



#IF YOU DO NOT WISH TO SEND ANY PDF, COMMENT OUT LINES 29 AND 30 AS WELL AS LINES 43-44
with open('MY_PDF.pdf', 'rb') as content_file:
    content = content_file.read()

# Add SSL (layer of security)
context = ssl.create_default_context()

# Loop through each recipient and send individual emails
for receiver in email_receivers:
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)
    #IF YOU DO NOT WISH TO SEND ANY PDF, COMMENT OUT LINES 43-44 AS WELL AS LINES 29 AND 30
    em.add_attachment(content, maintype='application',
                      subtype='pdf', filename='My_PDF.pdf')

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, receiver, em.as_string())
        print(f"Email sent to {receiver}")



print("All emails sent.")
