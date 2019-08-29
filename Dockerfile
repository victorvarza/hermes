FROM python:3.7.4-slim-buster

MAINTAINER Victor Varza <victor.varza@gmail.com>

COPY app/ /app
COPY docker-entrypoint.sh /
COPY requirements.txt /

RUN pip install -r /requirements.txt
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT [ "/docker-entrypoint.sh" ]