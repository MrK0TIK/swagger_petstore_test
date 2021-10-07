import requests
import urllib3

URL = 'https://petstore.swagger.io/v2/swagger.json'
_session = requests.session()


def post_function(data):
    x = _session.post(URL, data)
    print("-----request begins-----\n")
    print(x.request.body)
    print("\n-----request ends-----\n")
    print("-----response begins-----\n")
    print(x.text)
    print("\n-----response ends-----\n")
    return x


def put_pet():
    data = {"id": 0,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [{
                "id": 0,
                "name": "string"
            }],
            "status": "available"
            }

    response = post_function(data)
    print(response.status_code)

put_pet()
