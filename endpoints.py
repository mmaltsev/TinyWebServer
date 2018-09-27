# -*- coding: utf-8 -*-
"""A module for describing endpoints of the server.

First, this module introduces multiple constants fetched from the file `config.json`.
Next, all endpoints with their functionality are described in respective methods.
Description of each endpoint should be the following:
  - names of the methods MUST reflect names of respective endpoints, where all slashes ('/')
    in each endpoint path are substituted with underscores ('_').
    Example: /api/v0/endpoints (endpoint path) => _api_v0_endpoints (method name)
  - each method MUST return three values:
      * a byte string of data
      * mime_type of the file
      * status code of the request
At last, three default methods are introduced:
  - static(path), which simply returns the content of the file, available at this path.
  - server_error(), which returns a 404 error message, according to HTTP standards (https://tools.ietf.org/html/rfc7231)
  - client_error(), which returns a 400 error message, according to HTTP standards (https://tools.ietf.org/html/rfc7231)
"""
import json

# Global constants initialization #
STATUS_CODES = {
    'success': 200,
    'error': 404,
    'client_error': 400
}
with open('config.json') as f:
    CONFIG = json.load(f)


def _():
    """Handle '/' endpoint."""
    f = open('frontend/index.html', 'rb')
    return f.read(), 'text/html', STATUS_CODES['success']


def _example():
    """Handle '/example' endpoint."""
    f = open('data/example.json', 'rb')
    return f.read(), 'application/json', STATUS_CODES['success']


def mime_type_map(format):
    """Map file names to mime types."""
    if format == 'css':
        return 'text/css'
    elif format == 'js':
        return 'text/javascript'
    elif format == 'png':
        return 'image/png'
    elif format == 'jpeg' or format == 'jpg':
        return 'image/jpeg'
    else:
        return 'text/plain'


def static(path):
    """Handle static files requests."""
    path = path[1:]  # removing first slash (/)
    try:
        f = open(path, 'rb')
        format = path.split('.')[-1]
        mime_type = mime_type_map(format)
        return f.read(), mime_type, STATUS_CODES['success']
    except Exception:
        return server_error()


def server_error():
    """Handle server errors (return 404 code)."""
    return CONFIG['404'].encode('utf-8'), 'text/html', STATUS_CODES['error']


def client_error():
    """Handle client errors (return 400 code)."""
    return CONFIG['400'].encode('utf-8'), 'text/html', STATUS_CODES['client_error']
