# -*- coding: utf-8 -*-
"""A module for describing helper functions for the web server.

First, this module introduces multiple constants fetched from the file `config.json`.
Then, three default methods are introduced:
  - static(path), which simply returns the content of the file, available at this path.
  - server_error(), which returns a 404 error message, according to HTTP standards (https://tools.ietf.org/html/rfc7231)
  - client_error(), which returns a 400 error message, according to HTTP standards (https://tools.ietf.org/html/rfc7231)
At last, helper functions are implemented.
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


def static(path):
    """Handle static files requests."""
    file_path = path[1:]  # removing first slash ('/')
    return request(file_path)


def server_error():
    """Handle server errors (return 404 code)."""
    return CONFIG['404'].encode('utf-8'), 'text/html', STATUS_CODES['error']


def client_error():
    """Handle client errors (return 400 code)."""
    return CONFIG['400'].encode('utf-8'), 'text/html', STATUS_CODES['client_error']


def read_file(file_path):
    """Read file by the path."""
    f = open(file_path, 'rb')
    return f.read()


def mime_type_map(format):
    """Map file names to mime types."""
    if format == 'css':
        return 'text/css'
    elif format == 'js':
        return 'text/javascript'
    elif format == 'json':
        return 'application/json'
    elif format == 'html':
        return 'text/html'
    elif format == 'png':
        return 'image/png'
    elif format == 'jpeg' or format == 'jpg':
        return 'image/jpeg'
    else:
        return 'text/plain'


def get_mime_type(file_path):
    """Get mime type out of the file path."""
    format = file_path.split('.')[-1]
    return mime_type_map(format)


def request(file_path):
    """Request file by the file path."""
    try:
        data = read_file(file_path)
        mime_type = get_mime_type(file_path)
        return data, mime_type, STATUS_CODES['success']
    except Exception:
        return server_error()
