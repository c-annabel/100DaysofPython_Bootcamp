#SMTP protocol client: https://docs.python.org/3/library/smtplib.html
#Date & Time: https://docs.python.org/3/library/datetime.html
# Gmail: smtp.gmail.com
# Outlook: outlook.office365.com
import random
#Email SMTP

import smtplib

my_email = "zheng.annabel@gmail.com"
password = "ittlbwkgiojwnwiq"

#Create 2-way authentication, and create & copy the App password ittlbwkgiojwnwiq

# connection = smtplib.SMTP("smtp.gmail.com")
# #TLS: TransportLayerSecurity
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="ac.destinee@gmail.com",
#                     msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()

# #SEcond way:
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="ac.destinee@gmail.com",
#         msg="Subject:Hello2\n\nThis is the body of my email."
#     )

# DateTime Module
# import datetime as dt
#
# now = dt.datetime.now()
# print(now)
# print(type(now))
# print(now.year)
# print(type(now.year))
# year = now.year
# day_of_week = now.weekday()
# if year == 2020:
#     print("Wear a face mask")
# print(day_of_week)
# print(now.date)
# print(now.day)
#
# date_of_birth = dt.datetime(year= 1995 , month=12 , day=15, hour=4 ) #hours need specific input
# print(date_of_birth)

#Challenge 1 Send Motivational Quotes on Mondays via Email

import smtplib
import datetime as dt

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt")  as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ac.destinee@gmail.com",
            msg=f"Subject:Test Python EmailSmtp 01\n\n{quote}"
        )