from flask import Flask,render_template,request,redirect,url_for
from dotenv import load_dotenv
import os
import requests
import random

app = Flask(__name__)
load_dotenv()
key = str(os.environ.get('API_KEY'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mars',methods=['GET'])
def mars():
    url='https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key='+key
    response = requests.get(url).json()

    links = []
    for i in response["photos"]:
        links.append(i['img_src'])

    dice = random.randint(0,len(links))
    picture = links[dice]

    return render_template('mars.html',picture=picture)

@app.route('/potd',methods=['GET'])
def potd():
    url='https://api.nasa.gov/planetary/apod?api_key='+key
    response = requests.get(url).json()

    picture = response["hdurl"]
    text = response["explanation"]
    return render_template('potd.html',picture=picture,text=text)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')