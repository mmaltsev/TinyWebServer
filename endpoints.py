# -*- coding: utf-8 -*-
"""A module for describing endpoints of the server.

All endpoints with their functionality are described in respective methods.
Description of each endpoint should be the following:
  - names of the methods MUST be unique and HAVE TO reflect in the "method_name" property of
  the respective endpoint in the file config.json.
  - each method MUST return three values:
      * a byte string of data
      * mime_type of the file
      * status code of the request
"""
import helpers
import json


def _():
    """Handle '/' endpoint."""
    file_path = 'frontend/index.html'
    return helpers.request(file_path)


def _one():
    """Handle '/one' endpoint."""
    file_path = 'data/one.json'
    return helpers.request(file_path)


def _two():
    """Handle '/example' endpoint."""
    dict_data = {"two": 2}
    json_data = json.dumps(dict_data, indent=4, separators=(',', ': '))
    bytes_data = json_data.encode('utf-8')
    return bytes_data, helpers.mime_type_map('json'), helpers.STATUS_CODES['success']

def _parking():
    file_path = 'data/parking.json'
    return helpers.request(file_path)

def _geojson():
    file_path = 'data/neues_tor.geojson'
    return helpers.request(file_path)

def _swisscities():
    file_path = 'data/swisscities.csv'
    return helpers.request(file_path)

def _smoke():
    file_path = 'data/smoke.gif'
    return helpers.request(file_path)
