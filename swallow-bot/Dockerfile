FROM python:2.7

ADD ./ /bot
RUN pip install -r /bot/requirements.txt

WORKDIR /bot
ENTRYPOINT ["python", "swallowws_bot.py"]
