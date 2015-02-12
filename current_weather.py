import os
import pynotify
import time
import requests
import json

import config

parentdir = os.path.dirname(os.path.realpath(__file__))
current_time = time.strftime("%d_%m_%Y_%H_%M")


def save_current_weather(city_id):
    response = requests.get(url=config.SERVER + "/data/2.5/weather?id=" + city_id + "&APPID=" + config.APPID)
    try:
        os.makedirs(parentdir + "/data/")
    except OSError:
        pass
    with open(parentdir + "/data/" + city_id + "_" + current_time + ".json", 'w') as data_file:
        json.dump(response.json(), data_file)


def get_weather(city_id):
    icons_url = "http://openweathermap.org/img/w/"
    save_current_weather(city_id)
    with open(parentdir + "/data/" + city_id + "_" + current_time + ".json") as weather_file:
        weather_data = json.load(weather_file)
    city = weather_data["name"]
    icon = parentdir + "/icons/" + weather_data["weather"][0]["icon"] + ".png"
    description = weather_data["weather"][0]["description"]

    # Tempature in C
    temperature = str(weather_data["main"]["temp"] - 273.15)

    return city, str(temperature) + u"\u2103", icon, description


def weather_notification(title_text, text, icon):
    pynotify.init("Basics")
    n = pynotify.Notification(title_text, text, icon)
    n.show()


weather = get_weather(config.KYIVID)
city = weather[0]
temperature = weather[1]
weather_icon = weather[2]
weather_description = weather[3]

weather_notification(city, temperature + ", " + weather_description, weather_icon)
