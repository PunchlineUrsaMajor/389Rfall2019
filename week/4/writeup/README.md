# Writeup 2 - Pentesting

Name: Charlie Schneider
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charles Schneider

## Assignment Writeup

### Part 1 (45 pts)

Flag: CMSC389R-{p1ng_as_a_$erv1c3}

First, I ran `$ nc wattsamp.net 1337` to see what the prompt looked like. It seemed like it was just asking for an IP address to feed to the ping command, then sending back the output. Knowing that the vulnerability is command injection, I searched around for pentesting information about command injection, and found that an insecure service that processes raw input might be vulnerable. Assuming the service is just running `$ ping <user input>`, I could just add a `; <command>` to execute arbitrary commands and see the output. Sure enough, passing `8.8.8.8; ls` (the ping IP does not matter, 8.8.8.8 is always up anyway) returning the directory listing of the server's root folder. Since the flag was in /home last time, I tried `8.8.8.8; ls home`, which showed a `flag.txt` in the /home directory, so `8.8.8.8; cat home/flag.txt` returned the contents of the flag. 

If Eric wanted to secure this service, there are a few things he could do. It is generally best practice to "sanitize" your inputs and try to filter out possibly malicious or otherwise invalid input. At the very least, since Eric knows the input should just be an IPv4 address, he could try to match the input to a regular expression that matches IPv4 addresses (something like \d+\.\d+\.\d+\.\d+(:\d+)? to match an IP + port). He could even just reject any input that contains special characters like ';' or anything other than digits, periods, and colons. Another way Eric could secure this service is to restrict its permissions. My brief look at command injection shows that most command injection attacks can only run commands at the priviledge level of the service being exploited. If Eric's ping service was set to a very restricted priviledge level, for example, one that can only use ping, a command injection attack would not have the permissions to do much (unless it turns out that ping has a terrible vulnerability).

### Part 2 (55 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload your completed source code to this /writeup directory as well!*
