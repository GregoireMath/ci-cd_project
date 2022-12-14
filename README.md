# CI/CD Project - Grégoire MATHIAN & Yvann SENENTZ

## What is it ?

It is a little website which show you a random picture of Mars and a daily picture choose by Nasa.
We use for that the Nasa's API : https://api.nasa.gov

## Requirements

* python3&nbsp;&nbsp;```sudo apt install python3```
* pip3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```python3 -m pip3 install --upgrade pip```
* flask&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install flask```
* requests&nbsp;```pip3 install requests```
* dotenv&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install python-dotenv```

## Setup Locally

### Clone the project
```git clone git@github.com:GregoireMath/ci-cd_project.git```  

### Setup the API Key
```cd ci-cd_project```  
```echo 'API_KEY = "SECRET_KEY"' >> .env```

### Launch the app
```python3 app.py```  

## Website access

http://127.0.0.1:5000