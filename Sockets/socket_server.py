import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# In this example, socket.SOCK_DGRAM is a constant that
# designates that the socket should send the message over UDP
# recall that "Datagram" is the name of a message in UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
  data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
  print("received message: %s" % data)