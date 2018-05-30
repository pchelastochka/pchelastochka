# pchelastochka
Docker-based Web Tool For Weather Stations

### Description
* swallow-db:

MySQL containter for weather data storing

* swallow-weewx:

WeeWX-based container with own driver `swallow.py` for getting weather data

* swallow-bot

Telegram bot that that sends current weather data to users

* bee-db

MySQL containter for weather data storing

* bee-engine

python-driver for getting weather data

* bee-grafana

Grafana-based service for visualizing weather data

* web-common

All the web stuff for site

### Running
    systemctl start|stop pchelastochka.service
   
