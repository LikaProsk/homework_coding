FROM python:3.10-alpine


COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

ENV url "https://demo.opencart.com"
ENV browser "firefox"
ENV executor "127.0.0.1"
ENV drivers "lesson_5/drivers/linux"

CMD ["pytest", "tests/lesson_5", "--url", "127.0.0.1", "--browser", "chrome", "--executor", "127.0.0.1", "--drivers", "lesson_5/drivers/linux"]

