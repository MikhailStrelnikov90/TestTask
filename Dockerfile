FROM python:3.10.0-alpine

WORKDIR ./usr/Test_Task_Reqres

COPY . .

RUN apk add gcc xvfb chromium chromium-chromedriver firefox-esr curl

RUN curl -L https://github.com/mozilla/geckodriver/releases/download/v0.32.2/geckodriver-v0.32.2-linux64.tar.gz | tar xz -C /usr/local/bin

RUN pip3 install -r requirements.txt

CMD pytest --browser=chrome tests/*
