FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache git

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN set -ex && python -m pip install --no-cache-dir -r requirements.txt
COPY . /app
CMD ["python", "-m", "shotgunEventDaemon", "start"]
