FROM python:3.6-alpine3.7

MAINTAINER Victor Varza <victor.varza@gmail.com>

RUN apk update && pip install PyYAML PyDrive

# copy config files
COPY app/ /app
COPY docker-entrypoint.sh /

# set permissions
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT [ "/docker-entrypoint.sh" ]