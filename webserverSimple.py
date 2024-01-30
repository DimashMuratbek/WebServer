# Import the HTTP server module
import http.server
import socketserver

# Specify the port number you want to use
PORT = 8000

# Create a request handler by subclassing the BaseHTTPRequestHandler
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    # Override the do_GET method to customize the response
    def do_GET(self):
        # Set response code and headers
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Write the response content
        self.wfile.write(b"<html><head><title>My Local Web Server</title></head>")
        self.wfile.write(b"<body><h1>Welcome to My Local Web Server!</h1>")
        self.wfile.write(b"</body></html>")

# Create a TCP server with the specified port and request handler
with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("Server started on port", PORT)
    
    # Keep the server running until interrupted
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

# Server stopped
print("Server stopped")
