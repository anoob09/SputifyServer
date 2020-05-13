import json

import requests

from config import locationIQEndpointUrl, locationIQToken

def get_location_from_lat_long(latitude, longitude):
    response = requests.get("{}/v1/reverse.php?key={}&lat={}&lon={}&format=json".format(
            locationIQEndpointUrl, locationIQToken, latitude, longitude))
    if not response.ok:
        return None
    address = response.json().get("address")
    if address.get("city"):
        return address.get("city"), "city"
    if address.get("state"):
        return address.get("state"), "state"

def get_error_response(statusCode, message):
    return json.dumps({'success': False, 'message': message}), statusCode, {'ContentType': 'application/json'}

def get_success_response():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
