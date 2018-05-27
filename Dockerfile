FROM python:3.6-alpine3.7

MAINTAINER Victor Varza <victor.varza@gmail.com>

RUN apk update && \
    apk add --no-cache curl gcc g++ make libffi-dev openssl-dev && \
    curl -s -o /usr/local/bin/dumb-init -L https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 && \
    chmod +x /usr/local/bin/dumb-init &&\
    pip install PyYAML PyDrive &&\
    apk del gcc g++ make libffi-dev openssl-dev

# copy config files
COPY app/ /app
COPY docker-entrypoint.sh /

# set permissions
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT [ "/usr/local/bin/dumb-init", "/docker-entrypoint.sh" ]