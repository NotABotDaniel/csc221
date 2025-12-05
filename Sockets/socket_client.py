import socket

class Message:
    def __init__(self, MESSAGE, UDP_IP, UDP_PORT):
        self.UDP_IP = UDP_IP
        self.UDP_PORT = UDP_PORT
        self.MESSAGE = MESSAGE

    def __str__(self):
        return self.MESSAGE
    
ChrisIP = '196.xxx.1.124'

MESSAGE1 = Message(b"Hi, chris", ChrisIP, 5005)
# MESSAGE2 = Message(b"This is Daniel", ChrisIP, 5005)
# MESSAGE3 = Message(b"How ya doin?", ChrisIP, 5005)
messages = [MESSAGE1]
msg = messages[0]

for x in range(100):
  print("UDP target IP: %s" % msg.UDP_IP)
  print("UDP target port: %s" % msg.UDP_PORT)
  print("message: %s" % msg.MESSAGE)

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.sendto(msg.MESSAGE, (msg.UDP_IP, msg.UDP_PORT))  