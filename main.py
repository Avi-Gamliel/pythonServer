from PIL import Image
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import urllib.request
import os

def updateServerStatus(status):
    conditionsSetURL = '< put URL >'
    data = ''
    newConditions = {"data": data }
    params = json.dumps(newConditions).encode('utf8')
    req = urllib.request.Request(conditionsSetURL, data=params, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    return response


class Server(BaseHTTPRequestHandler):

    def _set_response(self):
        print(self)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("GET request")
        print("Path: " , str(self.path))
        print("Headers: ", str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):

        if self.Path == '/getData':
            # --> do somthing on this path


        # --> global post  in '/' :
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print("Path: " , str(self.path))
        print("Headers: ", str(self.headers))
        print("Data: ", post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=Server, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    updateServerStatus(True)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')
    updateServerStatus(False)

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
