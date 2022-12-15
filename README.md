# CI/CD Project - Grégoire MATHIAN & Yvann SENENTZ

## What is it ?

It is a little website which show you a random picture of Mars and a daily picture choose by Nasa.
We use for that the Nasa's API : https://api.nasa.gov

## How to run locally

### Requirements
* python3&nbsp;&nbsp;```sudo apt install python3```
* pip3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```sudo apt install python3-pip```
* flask&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install flask```
* requests&nbsp;```pip3 install requests```
* dotenv&nbsp;&nbsp;&nbsp;&nbsp;```pip3 install python-dotenv```

### Clone the project
```git clone git@github.com:GregoireMath/ci-cd_project.git```  

### Setup the API Key
```cd ci-cd_project```  
```echo 'API_KEY = "SECRET_KEY"' >> .env```

### Launch the app
```python3 app.py```  

### Website access
http://127.0.0.1:5000

## How to built with Docker

After install Docker and dependencies, you must create an image with the docker file:

### In the app's folder
```sudo docker build . -t <Image's Name>```

### Launch the docker
```sudo docker run -d -p 3232:5000 --name <Container's Name> <Image>```

### Website access
http://localhost:3232

## How to test
