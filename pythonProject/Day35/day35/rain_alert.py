import os
import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

acc_sid = "AC1078bca99d16f46ccf294d0878c9f83c"
token = "308c187003763577c3cb49d07915ba6a"
ph_no = "+13253089272"
my_no = "+917337043742"
client = Client(acc_sid, token)

api_key = "ae522d78380319de337cffd88ae90ab3"
parameters = {
    "lat": 27.2046,
    "lon": 77.4977,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}
api = f"https://api.openweathermap.org/data/2.5/onecall"
res = requests.get(url=api, params=parameters)
res.raise_for_status()
data = res.json()["hourly"]
for i in range(7, 19):
    if data[i]["weather"][0]["id"] < 700:
        message = client.messages \
            .create(
            body="Varsham padela undi, Godugu theskellu ☔️",
            from_=ph_no,
            to=my_no)
