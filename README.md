Simple weather notification for Ubuntu
===========================

Getting current weather notification  (based on http://openweathermap.org/)

Required python packages
--------------
* os
* pynotify
* time
* requests

How to run
--------------
1. Sign up on http://openweathermap.org/
2. Copy your APPID (API key) from http://openweathermap.org/my
3. Paste in config.py
4. Get CITYID from http://openweathermap.org
5. Set CITYID in config.py
4. git clone https://github.com/amazpyel/weather_notify.git ~/
5. cd ~/weather_notify
6. python get_current_weather.py
