import socket
import threading
import curses
import sqlite3 

target_ip = input("Target IP: ")
my_port = int(input("My Port: "))
target_port = int(input("Target Port: "))
my_name = input("What is your name?")

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

def main(stdscr):
  curses.echo() 
  chat_win = curses.newwin(20, 50, 0, 0)
  chat_win.scrollok(True)
  input_win = curses.newwin(5, 50, 21, 0)
  
  t = threading.Thread(target=listen, args=(chat_win,))
  t.daemon = True
  t.start()
  
  while True:
    input_win.clear()
    input_win.addstr(0, 0, "You: ")
    input_win.refresh()
    
    message = input_win.getstr().decode("utf-8")
    data = my_name + ":" + message
    
    if message == "exit":
      break
    
    s.sendto(data.encode("utf-8"), (target_ip, target_port))
    chat_win.addstr("Me: " + message + "\n")
    chat_win.refresh()

curses.wrapper(main)
