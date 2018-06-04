# pchelastochka
Docker-based Web Tool For Weather Stations

## Description
There are some **services** that run togeter.

* `swallow-db`:

MySQL containter for weather data storing

* `swallow-weewx`:

WeeWX-based container with own driver `swallow.py` for getting weather data

* `swallow-bot`:

Telegram bot that that sends current weather data to users

* `bee-db`:

MySQL containter for weather data storing

* `bee-engine`:

python-driver for getting weather data

* `bee-grafana`:

Grafana-based service for visualizing weather data

* `web-common`:

All the web stuff for site

## Running
* run all services:

`systemctl start|stop pchelastochka.service`
    
* run certain services:
```
cd /opt/pchelastochka
docker-compose restart <service-name1> <service-name2>
```    
* stop certain services:

`docker-compose stop <service-name1> <service-name2>`

## Site Customization
* `web-common/main/_posts/2014-09-21-services-1.markdown`:

This MD-file describes "swallow"

* `web-common/main/_posts/2014-09-21-services-2.markdown`:

This MD-file describes "bee"

* `web-common/main/_posts/2018-01-01-gallery.markdown`:

This file describes gallery.

* `web-common/main/index.html`:

This file contains page name and subname

* `web-common/main/_config.yml`:

This is main configuration file. There are some options: `url`, `title`, `stations` (links to station diagrams), `social` (different links)

* `web-common/main/_includes/about.html`:

This HTML-file describes *about info*

* `web-common/main/img`:

This directory stores all images (backgrounds, gallery, etc)

### How to update pictures

Put original images to `web-common/main/img/gallery`. Then, run `misc-tools/prepare_images.sh` to prepare images and update `web-2018-01-01-gallery.markdown`. This scripts crops images, creates thumbnails and inserts images list into `2018-01-01-gallery.markdown`.

### How to rebuild site?
After all manipulations with data in `web-common/main` you have to rebuild static site to generate your changes! Simply run `misc-tools/build_site.sh`.
