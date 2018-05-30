FROM python:2.7

COPY ./ /bee
RUN pip install -r /bee/requirements.txt

WORKDIR /bee
ENTRYPOINT ["python", "bee.py"]
