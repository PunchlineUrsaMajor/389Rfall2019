# Writeup 3 - OPSEC

Name: Charlie Schneider
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charles Schneider

## Assignment Writeup

### Part 1 (40 pts)

Given the nature of the questions, I think it would be best to frame the pretext as a fraud alert call from Eric's mother's bank. Assuming I could find Eric's mother's current name through OSINT, I could pose as an identity protection agent from some common bank (like Bank of America) that his mother likely has an account with. I could claim that there are large charges on his mother's account and abnormal web activity that suggest his mother's online banking account has been hacked, requiring immediate verification, but she has not responded, and Eric is listed as an emergency contact associated with the account. I would really stress the urgency of the issue, hopefully pressuring Eric to answer quickly and without much thought.  
First, I would claim to need to verify Eric's identity and association with his mother. I would ask some throwaway questions like "What is the zip code associated with this account?", "Are there any joint owners of this account?", and somewhere in there ask "Has your mother gone by any other names?", hopefully eliciting his mother's maiden name.  
Once finished with the "verification" questions, I can start trying to press for more information under the guise of correcting malicious edits to her account. "It seems there have been a few recent logins from unusual locations, does access from Internet Explorer in the Denver area sound correct?" Hopefully this would elicit what browser his mother usually uses.  
I could also claim that the attacker edited some security questions to prevent Eric's mother from reseting her password, asking Eric to verify if the answers to some questions are correct.  
I could ask standard questions like "It says the make and model of her first car was a Honda Civic, is this correct?" and ask for any corrections. Continuing, I could ask "It says here she was born in Buffalo, New York, does that seem right?", and maybe "The last question says the name of her first pet was Mr. Doodle", hopefully getting most of that information.  
Finally, I would claim that the ATM's pin number has been changed, and ask Eric to provide the previous PIN to restore it. Hopefully this would give the final piece of information.  

This pretex has some issues, as later, Eric would likely tell his mother about this interaction, prompting her to possibly change her security questions and PIN number. Also, if Eric asks for personally identifiable information like the previous balance of his mother's account, I would have no way of answering correctly. In the worst case scenario, Eric is currently with his mom, blowing the whole thing to smithereens. Maybe in that case, I could claim that the number on file for his mom has a typo or something to that effect. Hopefully, the rushed nature of the questions would make Eric take little time to consider the logic of the situation.

### Part 2 (60 pts)

One of the first hits I found on Eric Norman was information from the Whois lookup of wattsamp.net. The whois lookup clearly showed his name, address, phone number, and email.
Most domain registering services like NameCheap offer something like WhoisGuard that replaces your public information in Whois with WhoisGuard's information, making it indistinguishable from any other domain using WhoisGuard.
Anyone can do a Whois lookup, and having information like your address and phone number can be dangerous, especially when associated with your company's website and admin server.  

Another major vulnerability was the fact that the admin server was accessible through port 1337, which was relatively easy to find and had no security (beyond a username and password).
If Eric Norman wanted to secure the 1337 port, he could have set some rule that only allowed a specific set of known IP addresses to access the port. It's unlikely that he would want many
machines to access that server, so he could limit access to something like his home machine, computers at work, etc. In addition, he could set a firewall rule that blocked access to port 1337, such that nmap would show that port as "filtered." If a general firewall rule showed nearly every other port as "filtered" as well, port 1337 would be mostly indistinguishable from any other non-standard port to nmap.
But, communicating with an admin server over netcat or sockets is poor security. It would be more secure to either use SSH through port 22 or continue to use SSH on port 1337. Continuing to use port 1337 would stop most random brute-force attacks against port 22. Considering Eric is sending a username and password over this connection, it should be secured.  

The final vulnerability that allowed me to access Eric Norman's server was his week password. It was short (only 6 characters), and was just a dictionary word followed by a single digit. Even without the rockyou wordlist,
this password could be easily found with a dictionary attack. Even a pure brute-force attack, trying every combination of characters, would crack a 6-character password with a modest GPU-accelerated password cracking setup. 
A more robust password, especially one for a site's admin server, should be much longer (a minimum of 12 characters) and not contain any dictionary words. Ideally, a strong password would be a string of 16 or so random characters, which could be remembered through a password manager.
