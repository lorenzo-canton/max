from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import base64

hostName = "192.168.1.56"
serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = open("index.html", "r").read()
        self.wfile.write(bytes(html, "utf-8"))

    def do_POST(self):
        query = urlparse(self.path).query
        params = dict(qc.split("=") for qc in query.split("&"))

        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length).decode("utf-8")

        print(params)

        try:
            if params["enc"] == "true":
                print(content)
                base64_bytes = content.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                content = message_bytes.decode('ascii')
        except:
            pass
        print(content)
        
        
        f = open('save/%s.txt'%(params["title"]), "w")
        f.write(content)
        f.close()

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