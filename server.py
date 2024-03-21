from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import subprocess

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        code = data['code']
        try:
            result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, timeout=10)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(result)
        except subprocess.CalledProcessError as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(e.output)
        except subprocess.TimeoutExpired:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Execution timed out.")

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
