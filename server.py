# -*- coding: utf-8 -*-
"""A module for running a tiny web server.

First, constants are introduced, such as host and port of the server and list of endpoints.
Then, a functionality for the routing of comming requests is implemented.
After that, a class for the request handling is introduced.
At last, a method for running the server is described.
All functionality is implemented in Python 3.6.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import endpoints
import helpers

# Global constants initialization #
HOST, PORT, ENDPOINTS = helpers.CONFIG['HOST'], helpers.CONFIG['PORT'], helpers.CONFIG['ENDPOINTS']


def router(path, request_type, post_data=''):
    """Route requests."""
    if path in ENDPOINTS:
        if request_type == 'GET' and ENDPOINTS[path]['request_type'] == 'POST':
            return helpers.client_error()
        endpoint_method_name = ENDPOINTS[path]['method_name']
        endpoint_method = getattr(endpoints, endpoint_method_name)
        return endpoint_method()
    else:
        return helpers.static(path)
    return helpers.server_error()


class S(BaseHTTPRequestHandler):
    """Handle requests."""

    def _set_response(self, mime_type, status_code):
        """Send response and headers."""
        self.send_response(status_code)
        self.send_header('Content-type', mime_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        """Handle GET requests."""
        response_data, mime_type, status_code = router(self.path, 'GET')
        self._set_response(mime_type, status_code)
        self.wfile.write(response_data)

    def do_POST(self):
        """Handle POST requests."""
        content_length = int(self.headers['Content-Length'])  # size of the data
        post_data = self.rfile.read(content_length)  # data itself
        response_data, mime_type, status_code = router(self.path, 'POST', post_data)
        self._set_response(mime_type, status_code)
        self.wfile.write(response_data)


def run(host=HOST, port=PORT, server_class=HTTPServer, handler_class=S):
    """Execute web server."""
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        print('Tiny Web Server is up at {}:{}'.format(host, port))
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


run(HOST, PORT)
