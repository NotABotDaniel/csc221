import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# server
sock = socket.socket(socket.AF_INET,
                      socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
     data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
     print("received message: %s" % data)


# client

MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET,
                    socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

# curses
import curses

def main(stdscr):
    # Setup
    curses.echo() #make the input visible
    height, width = (24,80) #we're hard-coding this for now. 
                            #make sure you manually adjust to 24x80 
                            #before running

    
    # Create a window to display the chat history
    chat_height = height-3
    chat_win = curses.newwin(chat_height, width, 0, 0)
    
    # Create a window to type and read input
    input_win = curses.newwin(3, width, chat_height, 0)
    input_win.border()
    input_win.addstr(1, 2, "> ")
    input_win.refresh()
    
    messages = []
    
    while True:
        # Show user input
        curses.echo()

        #getstr moves the cursor to position (1,4) relative to this window,
        #  waits for the user to hit the enter key,
        # and then returns whatever the user typed.
        user_input = input_win.getstr(1, 4, width - 5).decode('utf-8').strip()
        
        #turn off user input until we're done updating the screen
        curses.noecho()
        
        if user_input:
            # Add your new message to the chat history
            messages.append(f"You: {user_input}")
            
            # Redraw full chat history
            chat_win.erase()
            for i, msg in enumerate(messages[-chat_height:]):
                chat_win.addstr(i, 0, msg)
            chat_win.refresh()
            
            # overwrite the previous input with a bunch of blanks
            input_win.addstr(1, 4, " " * (width - 5))
            input_win.refresh()

if __name__ == "__main__":
    curses.wrapper(main)