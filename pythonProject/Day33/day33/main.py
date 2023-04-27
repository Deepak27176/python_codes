import requests
import datetime as dt
import smtplib
MY_LAT = 16.515099
MY_LNG = 80.632095

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
iss_coordinates = (longitude, latitude)
print(iss_coordinates)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
present = dt.datetime.now()
hr = present.hour
# print(data)
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

if abs(latitude-MY_LAT) < 5 and abs(longitude-MY_LNG) <5:
    print("YES")
    # if hr > sunset or hr < sunrise:
    #     connect = smtplib.SMTP("smtp.gmail.com")
    #     connect.starttls()
    #     connect.login(user="yerramsettydeepak27176@gmail.com", password="Deep@k27176")
    #     connect.sendmail(from_addr="yerramsettydeepak27176@gmail.com",
    #                      to_addrs="yerramsettydeepak27176@gmail.com",
    #                      msg=f"Subject:ISS LOCATION\n\nlongitude: {longitude}\nlatitude: {latitude}")
else:
    print("NO")