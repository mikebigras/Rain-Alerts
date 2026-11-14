import requests
from twilio.rest import Client
import os

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = "+14014854110"
my_phone = "+15142950126"
API_KEY = os.environ.get("OWM_API_KEY")
print(API_KEY)
LAT = 45.8500      # Mascouche
LON = -73.6500
OWN_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
CNT_ENTRIES = 4

parameters = {
    "lat": LAT,
    "lon": LON,
    "cnt": CNT_ENTRIES,
    "appid": API_KEY,
    "units": "metric",  # températures en Celsius
    "lang": "fr"        # descriptions en français
}

response = requests.get(
    OWN_ENDPOINT,
    params=parameters
)

response.raise_for_status()

weather_data = response.json()

#print(weather_data["list"][0]["weather"][0]["description"])
#print(weather_data["list"])
will_rain = False
for entry in weather_data["list"]:
    #print(entry["weather"][0]["id"])
    if int(entry["weather"][0]["id"]) < 900:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring your ☂️",
        from_=twilio_phone,  # Votre numéro Twilio (format E.164, ex: +15551234567)
        to=my_phone,  # Le numéro de destinataire (ex: +15559876543)
    )

    print(f"Message send with success ! SID du message : {message.sid}")
