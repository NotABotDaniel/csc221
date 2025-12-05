import socket

class Message:
    def __init__(self, MESSAGE, IP, PORT):
      self.IP = IP
      self.PORT = PORT
      self.MESSAGE = MESSAGE

    def __str__(self):
      return self.MESSAGE
    
    def send(self):
      # print("UDP target IP: %s" % self.UDP_IP)
      # print("UDP target port: %s" % self.UDP_PORT)
      # print("message: %s" % self.MESSAGE)

      sock.sendto(self.MESSAGE, (self.IP, self.PORT))
      print('message sent')
    
    def encode(self):
      self.IP = str(self.IP).encode()

class computer:
  def __init__(self, ip, port):
    self.ip = ip
    self.port = port

receiver = computer('127.0.0.1', 2048)
adam = computer('idk.idk.idk.idk', 5005)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((receiver.ip, receiver.port))

who = input('message target: ')
if who == 'adam':
  target = adam
elif who == 'self':
  target = receiver

while True:
  m = input('send message: ')
  newMessage = Message(m.encode(), target.ip, target.port)
  newMessage.encode()
  newMessage.send()
  
  data, addr = sock.recvfrom(1024)
  print("received message: %s" % data)