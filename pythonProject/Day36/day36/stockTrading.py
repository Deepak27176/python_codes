STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
import smtplib
my_mail ="yerramsettydeepak27176@gmail.com"
mail_pass = "Deep@k27176"
receiver = "deepakyerramsetti@gmail.com"
stock_api_key = "HSDUIQVVFAAR256B"
news_api_key = "61be75c2524b4897950d497b4dd1d01e"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "interval": "5min",
    "apikey": stock_api_key

}
news_params = {
    "apiKey": news_api_key,
    "qInTitle": COMPANY_NAME
}
#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
res = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
res.raise_for_status()
data = res.json()
daily_data = data["Time Series (Daily)"]
yesterday = ""
day_before_yesterday = ""
flag = 0
#TODO 2. - Get the day before yesterday's closing stock price
for (key, value) in daily_data.items():
    if flag > 1:
        break
    else:
        if flag == 0:
            yesterday = value
            flag += 1
        elif flag == 1:
            day_before_yesterday = value
            flag += 1
yesterday_closing_price = float(yesterday["4. close"])
d_b_y_closing_price = float(day_before_yesterday["4. close"])


#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
change_in_stock = yesterday_closing_price - d_b_y_closing_price
change_in_stock = change_in_stock/yesterday_closing_price
change_in_stock = change_in_stock*100

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
   # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(change_in_stock) > 5:
    if change_in_stock > 5:
        subject = f"Stock Alert 🚨 TESLA 🔺{round(abs(change_in_stock), 2)}"
    else:
        subject = f"Stock Alert 🚨 TESLA 🔻{round(abs(change_in_stock),2)}"

    response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    response.raise_for_status()
    articles = response.json()["articles"][:3]
    msg1 = f"HeadLine: {articles[0]['title']}\nBrief: {articles[0]['description']}\nResource: {articles[0]['url']}"
    msg2 = f"HeadLine: {articles[1]['title']}\nBrief: {articles[1]['description']}\nResource: {articles[1]['url']}"
    msg3 = f"HeadLine: {articles[2]['title']}\nBrief: {articles[2]['description']}\nResource: {articles[2]['url']}"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_mail, password=mail_pass)
    connection.sendmail(from_addr="yerramsettydeepak27176@gmail.com",
                        to_addrs=receiver,
                        msg=f"Subject:{subject}\n\n{msg1}")
    connection.sendmail(from_addr="yerramsettydeepak27176@gmail.com",
                        to_addrs=receiver,
                        msg=f"Subject:{subject}\n\n{msg2}")
    connection.sendmail(from_addr="yerramsettydeepak27176@gmail.com",
                        to_addrs=receiver,
                        msg=f"Subject:{subject}\n\n{msg3}")
    connection.close()

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python or send mail by using smtplib
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

