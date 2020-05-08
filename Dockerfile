FROM python:3.6

ADD . .
WORKDIR /

RUN apt update -y && \
    apt install -y python-pip python-dev

COPY . .

RUN pip install -r requirements.txt

CMD python app.py
CMD flask db init && \
    flask db migrate && \
    flask db upgrade