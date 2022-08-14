from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

hostName = "192.168.1.24"
serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = open("index.html", "r").read()
        self.wfile.write(bytes(html, "utf-8"))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        print(self.rfile.read(content_length).decode("utf-8"))

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = open("index.html", "r").read()
        self.wfile.write(bytes(html, "utf-8"))
        

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")