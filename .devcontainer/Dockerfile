ARG VARIANT="3.8.5-alpine3.12"
FROM python:${VARIANT}

RUN apk update && \
    apk upgrade && \
    apk add --no-cache \
    alpine-sdk \
    bash \
    git \
