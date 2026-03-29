import http.server#Imports: The necessary modules (http.server and socketserver).
import socketserver

PORT = 8000#Configuration: Sets the port number to 9000
Handler = http.server.SimpleHTTPRequestHandler# assigns SimpleHTTPRequestHandler as the request handler.

with socketserver.TCPServer(("", PORT), Handler) as httpd:#Creates a TCP server that listens on all available IP addresses ("") and the specified port (PORT), using SimpleHTTPRequestHandler to handle requests.
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
    #Running the Server: The server starts running and will continue to run, serving files from the current directory, until it is manually stopped.