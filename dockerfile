FROM python:3.11.1-buster
WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-pip

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install python-dotenv

COPY . .

CMD [ "python","app.py" ]