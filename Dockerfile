FROM python:3.10-alpine

WORKDIR /app


COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

ENV url "https://demo.opencart.com"
ENV browser "chrome"
ENV executor "selenoid"
ENV drivers "usr/local/bin"

CMD pytest tests/lesson_5 --alluredir=allure-results --url $url --browser $browser --executor $executor --drivers $drivers

