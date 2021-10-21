import requests
import api_functions


ApiFunctions = api_functions.ApiFunctions
url = 'https://petstore.swagger.io/v2/swagger.json'
_session = ApiFunctions.Session


def put_pet():
    request_data = dict()
    request_data['id'] = 0
    request_data['category'] = {'id': 0,
                                'name': 'string'
                                }
    request_data['name'] = 'doggie'
    request_data['photoUrls'] = ['string']
    request_data['tags'] = [{'id': 0,
                             'name': 'string'
                             }]
    request_data['status'] = 'available'

    response = ApiFunctions.post_function(url, request_data)
    print(response.status_code)


put_pet()
