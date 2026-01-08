import socket
import threading
import curses
import sqlite3 

addresses = []

class address:
  def __init__(self, ip, port):
    self.ip = ip
    self.port = port

class chat:
  def initiateConversation():
    my_port = int(input("Enter your Port: "))
    my_name = input("Enter your name: ")

    while True:
      newIP = input("Enter target IP: ")
      newPort = input("Enter target Port: ")
      addresses.append(address(newIP, newPort))
      
      if input("(y/n) Add another address? ") != "y":
        break
    return my_port, my_name

  def listen(window, socket):
    while True:
      try:
        data, addr = socket.recvfrom(1024)
        text = data.decode("utf-8")
        name, text = text.split(":", 1)
        window.addstr(name + ": " + text + "\n")
        window.refresh() 
      except:
        break
      
  def startListenThread(window, socket):
    t = threading.Thread(target=chat.listen, args=(window,socket,))
    t.daemon = True
    t.start()

  def promptForMessage(window):
    window.clear()
    window.addstr(0, 0, "You: ")
    window.refresh()
    
    return window.getstr().decode("utf-8")

  def send(window, message, my_name, socket):
    data = my_name + ":" + message
      
    for target in addresses:
      socket.sendto(data.encode("utf-8"), (target.ip, target.port))

    window.addstr("Me: " + message + "\n")
    window.refresh()

  def startMessageing(input_win, chat_win, my_name, socket):
    while True:
      message = chat.promptForMessage(input_win)
      if message == "exit":
        break
      
      chat.send(chat_win, message, my_name, socket)
  
def main(stdscr):
  my_port, my_name = chat.initiateConversation()
  
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.bind(("0.0.0.0", my_port))

  curses.echo() 
  chat_win = curses.newwin(20, 50, 0, 0)
  chat_win.scrollok(True)
  input_win = curses.newwin(5, 50, 21, 0)
  
  chat.startListenThread(chat_win, s)
  chat.startMessageing(input_win, chat_win, my_name, s)

curses.wrapper(main)
