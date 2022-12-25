import pytest
import requests
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index(client):
    response = client.get('http://localhost:3232/')
    assert response.status_code == 200

def test_mars(client):
    response = client.get('http://localhost:3232/mars')
    assert response.status_code == 200

def test_potd(client):
    response = client.get('http://localhost:3232/potd')
    assert response.status_code == 200