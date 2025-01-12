#!/usr/bin/env python3
#
# The *echo server* is an HTTP server that responds to a GET request by
# sending the query path back to the client.  For instance, if you go to
# the URI "http://localhost:8000/Balloon", the echo server will respond
# with the text "Balloon" in the HTTP response body.
#
# Instructions:
#
# The starter code for this exercise is the code from the hello server.
# Your assignment is to change this code into the echo server:
#
#   1. Change the name of the handler from HelloHandler to EchoHandler.
#   2. Change the response body from "Hello, HTTP!" to the query path.
#
# When you're done, run it in your terminal.  Try it out from your browser,
# then run the "test.py" script to check your work.

from http.server import HTTPServer, BaseHTTPRequestHandler

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # response
        self.send_response(200)
        
        # header, specifying what type to send back
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # response body
        self.wfile.write(self.path.encode())

if __name__ == "__main__":
    # specify where the server is hosted
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, EchoHandler)
    httpd.serve_forever()



