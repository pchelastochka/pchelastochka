FROM python:2.7

# add weewx dist
# ADD weewx /weewx

# add driver
# ADD swallow.py /weewx/bin/weewx/drivers/swallow.py

RUN pip install pyserial MySQL-python Cheetah Pillow

# python cannot see modules without it
ENV PYTHONPATH /usr/local/lib/python2.7/site-packages

# ENTRYPOINT ["/weewx/bin/weewxd", "/weewx/weewx.conf"]
