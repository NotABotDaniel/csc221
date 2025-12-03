# Django

Date: 12-01-2025

## django for everybody

### big picture
User action triggers a request for data that is sent from the browser to the web server and the django aplication. The request is proccessed through the django, a bunch of stuff happens, maybe accesses a database. Then information is sent back to the browser where it proccesses the response and displays it to the user.

### little deeper
- Python is an aplication listening for a request
- When receives request, looks at several files (urls.py, etc...)
- aplication starts with settings.py

### settings.py
"ALLOWED_HOSTS = ['\*']" (I know from past experience that '\*' means 'everywhere')

This line represents a filter for incoming requests.

- "INSTALLED_APPS" : define all  applications 
- "ROOT_URLCONF"   : load the url
- "urlpatterns"    : global url routing


## Web application and request/response cycle

### applications used
- Front end : done in your web browser: html,css,dom,javascript,jquery
- Back end  : done on the web server: django/flask, sqlite3/mysql

### request response cycle
Your browser sends a request, the server responds. (detailed in "big bicture" section of prev vid)

- GET  : requesting for data to be sent back
- POST : requesting for the server to do something with the data you send it


## Network Sockets
Like phones for computers

### TCP connections / sockets
The connection that computers use to communicate.

Needs protocols to communicate properly.
Needs a handshake to secure connection.

Used to start with this digital handshake sound: 
blooEEEEEEEoooooo-wakdawakdawakda-kkkkkkkkk-bedldeepbedldeep-SKIIIIIIIRRRR-kkssssshhhhhhh etc...

### TCP port numbers
- Every computer has an IP address.
- Port numbers are application-specific addresses witin a system.


## Hyper text transfer protocol (http)
How browsers talk to servers (and much more)

### uniform recourse locator
consists of: protocol://host/document

example: http://example.com/page.html

### internet standars
- preposed in 1981, we have a set of protocol spesifications
- called RFCs
- No one owns the internet! (yay)


## Simple python web browser
What happens on your end

### To open a file
1. Create a socket
2. Secure a connection (try and exept cuz in might err)
4. Encode a command (GET requesst)
5. Send the command
6. Wait (or don't) for incoming data
7. Receive incoming data
8. Repeat 6 and 7
9. Decode data

### Yay?
Yay


## Simple python web server
What happens on their end

### To respond to a request
By default, server is waiting for incoming requests

1. See something incoming
2. declare acceptable port number
3. If port is in use, que incoming requests
4. Wait for secure connection
5. ...

This is unfinished

