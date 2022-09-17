FROM python:3.10-alpine

RUN apk update && apk add --no-cache bash \
        chromium \
        chromium-chromedriver

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

ENV url "https://demo.opencart.com"
ENV browser "chrome"
ENV executor "127.0.0.1"
ENV drivers "usr/bin/"

CMD pytest tests/lesson_5  --url $url --browser $browser --executor $executor --drivers $drivers

