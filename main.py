from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Salom, dunyo!'

@app.route('/about', methods=['GET'])
def about():
    return 'Bu veb-serverning haqida ma\'lumot.'

@app.route('/contact', methods=['GET'])
def contact():
    return 'Iltimos, biz bilan bog\'laning.'

if __name__ == '__main__':
    app.run(debug=True)
```

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Salom, dunyo!')
        elif self.path == '/about':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Bu veb-serverning haqida ma\'lumot.')
        elif self.path == '/contact':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Iltimos, biz bilan bog\'laning.')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Not found.')

def run_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Server started on port 8000...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
