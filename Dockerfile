FROM python:3

COPY . /RobotzSite
WORKDIR /RobotzSite

RUN pip install -r requirements.txt

CMD python main.py
