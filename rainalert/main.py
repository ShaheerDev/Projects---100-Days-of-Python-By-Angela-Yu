import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "#Your Api Key"
account_sid = "#You Account Sid"
auth_token = "#You auth Token"
client = Client(account_sid, auth_token)

weather_params = {
    "lat": 24.8607,
    "lon": 67.0011,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        break
if will_rain:
    message = client.messages.create(
        body="It going to rain today remember to bring an umbrella ☔",
        from_='whatsapp:+14155238886',
        to='whatsapp:+923110241413',
    )
    print(f"Message sent {message.status}")

# if weather_data["list"][0]["weather"][0]["id"] < 800:
#     print("its going to rain")
#
# if weather_data["list"][1]["weather"][0]["id"] < 800:
#     print("its going to rain")
#
# if weather_data["list"][2]["weather"][0]["id"] < 800:
#     print("its going to rain")
#
# if weather_data["list"][3]["weather"][0]["id"] < 800:
#     print("its going to rain")
# weather_data = responce.json()
# if weather_data["list"][4]["weather"][0]["id"] < 800:
#     print("its going to rain")
#
# if weather_data["list"][5]["weather"][0]["id"] < 800:
#     print("its going to rain")
#
# if weather_data["list"][6]["weather"][0]["id"] < 800:
#     print("its going to rain")
#
# if weather_data["list"][7]["weather"][0]["id"] < 800:
#     print("its going to rain")
