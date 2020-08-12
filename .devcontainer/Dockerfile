ARG VARIANT="3.8.5-alpine3.12"
FROM python:${VARIANT}

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    alpine-sdk \
    libxml2-dev \
    libxslt-dev \
    bash \
    git \
    nodejs \
    nodejs-npm \
    expect

RUN npm install -g atcoder-cli
RUN acc config default-task-choice all && \
    acc config default-test-dirname-format test

COPY .devcontainer/template/main.py /root/.config/atcoder-cli-nodejs/python/main.py
COPY .devcontainer/template/template.json /root/.config/atcoder-cli-nodejs/python/template.json
