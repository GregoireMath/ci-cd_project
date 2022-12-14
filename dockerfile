WORKDIR /app

RUN apt-get update
RUN apt-get install -y python3-pip

#COPY requirements.txt ./

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install python-dotenv

COPY . .

#ENTRYPOINT [ "python" ]

CMD [ "python","app.py" ]


