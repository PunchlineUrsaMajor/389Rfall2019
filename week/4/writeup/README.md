# Writeup 2 - Pentesting

Name: Charlie Schneider
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charles Schneider

## Assignment Writeup

### Part 1 (45 pts)

Flag: CMSC389R-{p1ng_as_a_$erv1c3}

First, I ran `$ nc wattsamp.net 1337` to see what the prompt looked like. It seemed like it was just asking for an IP address to feed to the ping command, then sending back the output. Knowing that the vulnerability is command injection, I searched around for pentesting information about command injection, and found that an insecure service that processes raw input might be vulnerable. Assuming the service is just running `$ ping <user input>`, I could just add a `; <command>` to execute arbitrary commands and see the output. Sure enough, passing `8.8.8.8; ls` (the ping IP does not matter, 8.8.8.8 is always up anyway) returned the directory listing of the server's root folder. Since the flag was in /home last time, I tried `8.8.8.8; ls home`, which showed a `flag.txt` in the /home directory, so `8.8.8.8; cat home/flag.txt` returned the contents of the flag. 

If Eric wanted to secure this service, there are a few things he could do. It is generally best practice to "sanitize" your inputs and try to filter out possibly malicious or otherwise invalid input. At the very least, since Eric knows the input should just be an IPv4 address, he could try to match the input to a regular expression that matches IPv4 addresses (something like `\d+\.\d+\.\d+\.\d+(:\d+)?` to match an IP + port). He could even just reject any input that contains special characters like ';' or anything other than digits, periods, and colons. Another way Eric could secure this service is to restrict its permissions. My brief look at command injection shows that most command injection attacks can only run commands at the priviledge level of the service being exploited. If Eric's ping service was set to a very restricted priviledge level, for example, one that can only use ping, a command injection attack would not have the permissions to do much (unless it turns out that ping has a terrible vulnerability).

### Part 2 (55 pts)

Now, I had to write code to automatically use the exploit I found to execute arbitrary commands. The code (in shell.py) has a few layers. The top layer is the repl loop. It just prompts the user for input and looks for the 'shell' and 'pull' commands, anything else prints the help message. Additionally, it checks if the pull command has the right amount of arguments. If the shell command is run, it drops into another repl loop that communicates with the wattsamp server. Most commands are just sent to the server through the exploit. A socket connection is established, the code sends `8.8.8.8; <command>`, reads the return data, and discards the first few lines of the ping output. The tricky part is managing directories through the `cd` command. cd just changes the environment, and directory changes are not persistant across sessions, so I need to keep track of the current directory on my side of the code. If the user enters a cd command, it checks if it is just `cd`, and if so, sets the current directory to the top level `/`. If an argument is present, it will check if the argument is an absolute path, and set the directory to that path. If the argument is a relative path, it will iterate through the directories, doing nothing on `.`, popping a directory off the list on `..`, and adding a directory with anything else. Then, whenever a command is sent to the machine, I automatically add in a `cd` command to change to what the user has as the "current directory" before the user's command. The major problem with this is that it does not check if the current directory is actually a valid directory on the target machine.

The `pull` command is just a wrapper for sending the command to `cat` the requested file and write it to a local file. There are other methods of transferring files, like scp or even ftp, but scp requires authentication, and creating a link back to my machine seems like a bad idea in an attack scenario. Additionally, I could somehow use python sockets on the target machine to read and transfer the full file, but the ping service cannot create or edit files, and again, linking back to my machine seems like a bad idea. So, the major weakness of simply `cat`ing a file back is that the file might be larger than the amount of data I am expecting, but it is enough to retrieve the flag file.
