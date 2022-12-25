import requests


def test_http_request_menu():
    url = "http://localhost:3232/"
    response = requests.get(url)
    if response.status_code == 200:
        verification="OK"
    else:
        verification="NOK"

    return verification 


def test_http_request_potd():
    url = "http://localhost:3232/potd"
    response = requests.get(url)
    if response.status_code == 200:
        verification="OK"
        return verification
    else:
        raise Exception("Page error on /potd")


def test_http_request_mars():
    url = "http://localhost:3232/mars"
    response = requests.get(url)
    if response.status_code == 200:
         verification="OK"
    else:
        verification="NOK"
    return verification


test_http_request_mars()
test_http_request_potd()
test_http_request_menu()