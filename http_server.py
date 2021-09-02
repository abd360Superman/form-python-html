import http.server
import webbrowser

PORT = 6273
script_path = "cgi-bin/render_html.py"

server_class = http.server.HTTPServer
handler_class = http.server.CGIHTTPRequestHandler
server_address = ("", PORT)

httpd = server_class(server_address, handler_class)

url = 'http://localhost:{0}/{1}'.format(PORT, script_path)

webbrowser.open_new_tab(url)

print("serving at", url)

httpd.serve_forever()
