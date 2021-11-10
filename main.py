from selenium import webdriver
from selenium import webdriver
from time import sleep
import openpyxl
import pandas as pd
import email, smtplib, ssl
from random import randint
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import math

import emailtemplate
from vulnerablesettings import email1, password, file
from emailtemplate import html

# driver = webdriver.Chrome()

# TODO pozbyc sie tego
# settings
# email1 = 'oferta@fabryka-stron-gdansk.pl'
# password = '>3iLy-VD:y'
# file = 'kosmetyczkidata_samemaile.xlsx'


# content of the mail
mailcontent = [emailtemplate.html, emailtemplate.html1]

# TODO moze inne wczytywanie danych?
data = pd.read_excel(file)
df = pd.DataFrame(data, columns=['email'])
print(df)

subject = "Stworzymy dla Państwa stronę Internetową"
sender_email = email1
receiver_email = "oferta@fabryka-stron-gdansk"
# password = input("Type your password and press enter:")


print('0')
s = df['email']

print("ide spac do 8:00")
# sleep(16200)

# TODO schowac to do funkcji

lengthoftheList = len(s)
print(lengthoftheList)


# sending email by 50 each time


# function which builds 50 receviers each time
def BuildReceviersMime(x, y):  # x is number of iteration, y is how many emails we want to send at once

    b = slice(x, x+y)
    receiver_emaillist = ','.join(s[b])

    return receiver_emaillist


def BuildReceviersSMTP(x, y):
    b = slice(x, x+y)
    receiver_emaillist = s[b]
    print(receiver_emaillist)

    return receiver_emaillist


# BuildReceviers(0)


# text = message.as_string()
context = ssl.create_default_context()


def sendMails(lengthoftheList,sender_email,numberofemail, passedval=0 ):

    sleep(120)
    with smtplib.SMTP_SSL("hosting2138516.online.pro", 465, context=context) as server:
        server.login(sender_email, password)

        # loop for sending emails from database
        # for i in range(2288, 3655):  # we have already send 500 emails run1 (0,500) #also (500-100)
        while passedval < lengthoftheList:  # we have already send 500 emails run1 (0,500) #also (500-100) 2288
            try:
            # how many mails will be sent (random number beetwen 5 and 50)
                num1 = randint(5, 59)
                print("--------------------------------")
                print(num1)

                part2 = MIMEText(mailcontent[randint(0, 1)], "html")

                message = MIMEMultipart()
                message["From"] = sender_email
                message["To"] = receiver_email
                message["Subject"] = subject
                message["Bcc"] = BuildReceviersMime(passedval, num1)
                message.attach(part2)  # attaching mail content

                # function sending emails
                to = BuildReceviersSMTP(passedval, num1)
                sleep(5)
                server.sendmail(
                    sender_email, to, message.as_string()

                )
                print(str(num1) + "sent")
                passedval += num1
                print(passedval)
                sleep(randint(600, 1600))
                sendMails(lengthoftheList,sender_email,numberofemail,passedval)

            except:

                print("Spam allert")
                sleep(3)
                if(numberofemail == 0):
                    sender_email = "twojastrona@fabryka-stron-gdansk.pl"
                    numberofemail=1
                elif(numberofemail ==1):
                    sender_email = "oferta@fabryka-stron-gdansk.pl"
                    numberofemail=0
                               
                sendMails(lengthoftheList,sender_email,numberofemail,passedval)


sendMails(lengthoftheList,sender_email,0, 7)
