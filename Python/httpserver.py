import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import sys

HandlerClass = SimpleHTTPRequestHandler
ServerClass = BaseHTTPServer.HTTPServer
Protocol = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000

server_address = ('127.0.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

socket = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", socket[1], "..."
httpd.serve_forever()