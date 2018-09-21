# https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7C
# https://stackoverflow.com/questions/1094185/how-to-serve-any-file-type-with-pythons-basehttprequesthandler
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep

PORT = 8081

def router(path, request_type, post_data=''):
    if path == '/example' and request_type == 'GET':
        f = open('example.json', 'rb')
        return f.read(), 'application/json'
    return (request_type + ' request for {}'.format(path)).encode('utf-8'), 'text/html'


class S(BaseHTTPRequestHandler):
    def _set_response(self, mime_type='text/html'):
        self.send_response(200)
        self.send_header('Content-type', mime_type)
        self.end_headers()

    def do_GET(self):
        response_data, mime_type = router(self.path, 'GET')
        self._set_response(mime_type)
        self.wfile.write(response_data)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # size of data
        post_data = self.rfile.read(content_length)  # data itself
        response_data, mime_type = router(self.path, 'POST', post_data)
        self._set_response(mime_type)
        self.wfile.write(response_data)


def run(server_class=HTTPServer, handler_class=S):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd...')


run()
