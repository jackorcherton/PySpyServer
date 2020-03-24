#NOTE - as this is on a 'live' server - for security will only accept files named 'info.sqlite3'

import http.server, socketserver, io, cgi
import ssl
PORT = 443

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):#Placed this - as otherwise current directory displayed
        if self.path == '/':    self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        """Listens & waits for file"""
        successful = self.saveFile()
        reply = io.BytesIO()
        if successful:  reply.write(b"File Recieved Successfully")
        else:   reply.write(b"Something Went Wrong :(\nFile not saved!")
        length = reply.tell()
        reply.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", str(length))
        self.end_headers()
        if reply:
            self.copyfile(reply, self.wfile)
            reply.close()

    def saveFile(self):
        """Save's file"""
        ctype, pdict = cgi.parse_header(self.headers['Content-Type'])
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        pdict['CONTENT-LENGTH'] = int(self.headers['Content-Length'])
        if ctype == 'multipart/form-data':
            form = cgi.FieldStorage( fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'], })
            if (form["file"].filename)=="info.sqlite3":
                open("./%s"%form["file"].filename, "wb").write(form["file"].file.read())
                print(form["file"].filename)
                return True

ssl_key="/etc/letsencrypt/live/error404coventry.hopto.org/privkey.pem"
ssl_cert="/etc/letsencrypt/live/error404coventry.hopto.org/fullchain.pem"

Handler = CustomHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.socket=ssl.wrap_socket(httpd.socket, keyfile=ssl_key, certfile=ssl_cert, server_side=True)
    print("serving at port", PORT)
    httpd.serve_forever()