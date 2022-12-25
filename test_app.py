import pytest
import requests
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'index.html' in response.data

def test_mars(client):
    response = client.get('/mars')
    assert response.status_code == 200
    assert b'mars.html' in response.data

def test_potd(client):
    response = client.get('/potd')
    assert response.status_code == 200
    assert b'potd.html' in response.data