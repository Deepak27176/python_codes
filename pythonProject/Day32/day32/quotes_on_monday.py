import smtplib
import random
import datetime as dt
with open("quotes.txt", "r") as quotes:
    quotes_list = quotes.read()
    quotes_list = quotes_list.split("\n")
today = dt.datetime.now()
if today.weekday() == 0:
    quote = random.choice(quotes_list)
    sender = "yerramsettydeepak27176@gmail.com"
    password = "Deep@k27176"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(from_addr=sender,
                            to_addrs="deepakyerramsetti@gmail.com",
                            msg=f"Subject:donotreply\n\n {quote}")

