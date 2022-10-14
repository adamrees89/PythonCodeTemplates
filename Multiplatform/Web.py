## Credit to Haider Imtiaz
# Simple HTTP SERVER
import socketserver
import http.server
PORT = 8000
handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as http:
    print("Server Launch at Localhost: " + str(PORT))
    http.serve_forever()
# Type in http://127.0.0.1:8000/ in your webbrowser

#---------------------------------------------------
