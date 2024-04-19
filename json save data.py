# from http.server import BaseHTTPRequestHandler, HTTPServer
# import json

# class RequestHandler(BaseHTTPRequestHandler):
#     def _set_headers(self, status=200):
#         self.send_response(status)
#         self.send_header('Content-type', 'text/plain')
#         self.end_headers()

#     def do_POST(self):
#         content_length = int(self.headers['Content-Length'])
#         post_data = self.rfile.read(content_length)
#         data = json.loads(post_data)

#         with open('data.json', 'w') as f:
#             json.dump(data, f)

#         self._set_headers()
#         self.wfile.write("Data saved successfully".encode('utf-8'))

# def run(server_class=HTTPServer, handler_class=RequestHandler, port=3000):
#     server_address = ('', port)
#     httpd = server_class(server_address, handler_class)
#     print(f'Server is running on port {port}')
#     httpd.serve_forever()

# if __name__ == '__main__':
#     run()
