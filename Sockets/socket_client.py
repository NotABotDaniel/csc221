import socket

class Message:
    def __init__(self, MESSAGE, UDP_IP, UDP_PORT):
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.MESSAGE = MESSAGE

    def __str__(self):
        return self.MESSAGE

MESSAGE1 = Message(b"Hi, there", "127.0.0.1", 5005)
MESSAGE2 = Message(b"This is Daniel", "127.0.0.1", 5005)
MESSAGE3 = Message(b"How ya doin", "127.0.0.1", 5005)
messages = [MESSAGE1, MESSAGE2]

for msg in messages:
  print("UDP target IP: %s" % msg.UDP_IP)
  print("UDP target port: %s" %msg.UDP_PORT)
  print("message: %s" % msg.MESSAGE)

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.sendto(msg.MESSAGE, (msg.UDP_IP, msg.UDP_PORT))  