import socket
import threading
import curses
import sqlite3 

addresses = []
i = 0
message = ""
data = ""

class address:
  def __init__(self, ip, port):
    self.ip = ip
    self.port = port

my_port = int(input("Enter your Port: "))
my_name = input("Enter your name: ")

while True:
  newIP = input("Enter target IP: ")
  newPort = input("Enter target Port: ")
  addresses[i] = address(newIP, newPort)
  
  if input("(y/n) Add another address? ") == "y":
    i += 1
  else:
    break

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", my_port))

def listen(window):
  while True:
    try:
      data, addr = s.recvfrom(1024)
      text = data.decode("utf-8")
      name, text = text.split(":", 1)
      window.addstr(name + ": " + text + "\n")
      window.refresh() 
    except:
      break
    
def startListenThread(window):
  t = threading.Thread(target=listen, args=(window,))
  t.daemon = True
  t.start()

def promptForMessage(window):
  window.clear()
  window.addstr(0, 0, "You: ")
  window.refresh()
  
  message = window.getstr().decode("utf-8")

def send(window):
  data = my_name + ":" + message
    
  for target in addresses:
    s.sendto(data.encode("utf-8"), (target.ip, target.port))

  window.addstr("Me: " + message + "\n")
  window.refresh()

def startMessageing(input_win, chat_win):
  while True:
    promptForMessage(input_win)
    if message == "exit":
      break
    
    send(chat_win)
  
def main(stdscr):
  curses.echo() 
  chat_win = curses.newwin(20, 50, 0, 0)
  chat_win.scrollok(True)
  input_win = curses.newwin(5, 50, 21, 0)
  
  startListenThread(chat_win)
  startMessageing(input_win, chat_win)

curses.wrapper(main)
