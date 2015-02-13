import os
import requests

parentdir = os.path.dirname(os.path.realpath(__file__))
base_icons_url = "http://openweathermap.org/img/w/"
code = [
    "01d", "01n",
    "02d", "02n",
    "03d", "03n",
    "04d", "04n",
    "09d", "09n",
    "10d", "10n",
    "11d", "11n",
    "13d", "13n",
    "50d", "50n",
    ]


def dowload_icons():
    try:
        os.makedirs(parentdir + "/icons/")
        for i in range(len(code)):
            f = open(parentdir + "/icons/" + code[i] + ".png", 'wb')
            f.write(requests.get(base_icons_url + code[i] + ".png").content)
            f.close()
    except OSError:
        print "Icons are already available!"
