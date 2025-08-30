# EX01 Developing a Simple Webserver

## Date:30/08/2025

## AIM:

To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:

### Step 1:

HTML content creation.

### Step 2:

Design of webserver workflow.

### Step 3:

Implementation using Python code.

### Step 4:

Import the necessary modules.

### Step 5:

Define a custom request handler.

### Step 6:

Start an HTTP server on a specific port.

### Step 7:

Run the Python script to serve web pages.

### Step 8:

Serve the HTML pages.

### Step 9:

Start the server script and check for errors.

### Step 10:

Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:

'''

from http.server import HTTPServer, BaseHTTPRequestHandler

content ='''

<!doctype html>

<html>

    `<head>`

    `<meta charset="utf-8">`

    `<title>`saveetha experiment 1`</title>`

    `</head>`

    `<body>`

    `<table border="1" align="center" bgcolor="yellow" cellpadding="10">`

    `<caption><h1>`List of protocol`</h1></caption>`

    `<tr><th>`S.no`</th><th>`Name of the layer`</th><th>`Name of the protocol`</th></tr>`

    `<tr><td>`1`</td><td>`Application layer`</td><td>`HTML,RDP,DHCP,DNS,SMTP`</td></tr>`

    `<tr><td>`2`</td><td>`Transport layer`</td><td>`TCP&UDP`</td></tr>`

    `<tr><td>`3`</td><td>`Internet layer`</td><td>`IPV4,IPV6,ICMP`</td></tr>`

    `<tr><td>`4`</td><td>`Physical layer`</td><td>`Ethernet,Relay`</td></tr>`

    `</table>`

    `</body>`

</html>

classMyServer(BaseHTTPRequestHandler):

    defdo_GET(self):

    print("Get request received...")

    self.send_response(200)

    self.send_header("content-type","text/html")

    self.end_headers()

    self.wfile.write(content.encode())

print("This is my webserver")

server_address =('127.0.0.1',8000)

httpd =HTTPServer(server_address,MyServer)

httpd.serve_forever() '''

## OUTPUT:

![1756529150527](image/README/1756529150527.png)

## RESULT:

The program for implementing simple webserver is executed successfully.
