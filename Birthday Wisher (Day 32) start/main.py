
quotes_list = []
import datetime as dt
import random
import smtplib

now = dt.datetime.now()
current_day = now.weekday()
if current_day == 6:
    with open("quotes.txt") as data:
        quotes = data.readlines()
        for quote in quotes:
            quotes_list.append(quote)
        random_quote = random.choice(quotes_list)

my_email = "#Your Email"
password = "#Your Password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="#senders email",
        msg=f"Subject: Monday Quotes \n\n {random_quote}")
