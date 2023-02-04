#!/usr/bin/python

"""
Author: Dickson Agbemazi
Description: The program looks up location of some universities,
using a pseudo-Google GeoLocation API and parses the response
"""
import json
import urllib.request
import urllib.parse


API_URL = "http://py4e-data.dr-chuck.net/json?"
API_KEY = 42


def parse_location(address):

    parameters = dict()
    parameters['address'] = address
    if API_KEY is not False:
        parameters['key'] = API_KEY
    encoded_url = API_URL + urllib.parse.urlencode(parameters)
    api_call = urllib.request.urlopen(encoded_url)
    print(f"Retrieving {encoded_url}")

    load_geojson = json.load(api_call)
    place_id = load_geojson["results"][0]["place_id"]
    return f"Place ID: {place_id}"


location = input("Enter location: ")
response = parse_location(location)
print(response)
