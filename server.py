from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>saveetha experiment 1</title>
    </head>
    <body>
        <table border="1" align="center" bgcolor="yellow" cellpadding="10">
            <caption><h1>List of protocol</h1></caption>
            <tr><th>S.no</th><th>Name of the layer</th><th>Name of the protocol</th></tr>
            <tr><td>1</td><td>Application layer</td><td>HTML,RDP,DHCP,DNS,SMTP</td></tr>
            <tr><td>2</td><td>Transport layer</td><td>TCP&UDP</td></tr>
            <tr><td>3</td><td>Internet layer</td><td>IPV4,IPV6,ICMP</td></tr>
            <tr><td>4</td><td>Physical layer</td><td>Ethernet,Relay</td></tr>
        </table>
    </body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('127.0.0.1',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
