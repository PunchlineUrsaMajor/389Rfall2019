# Writeup 2 - OSINT

Name: Charlie Schneider
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charles Schneider

## Assignment Writeup

### Part 1 (45 pts)

1. ejnorman84's real name is Eric J. Norman. Found this by searching "ejnorman84" on DuckDuckGo, finding a pastebin listing his name and social media accounts. I also found a twitter profile under EricNorman84 from this pastebin.

2. ejnorman84 works at Wattsamp Electric as a Powerplant control specialist. This was on the @EricNorman84 twitter account. The website is https://wattsamp.net.

3. I found a Reddit account under ejnorman84, but I'm not sure how related that is. It was recently created so it is probably related. The twitter account also lists two emails: ejnorman84@gmail.com and ejnorman@protonmail.com. Running a whois search on wattsamp.net gives Eric's number (+1.2026562837) and address (1300 Adabel Dr. El Paso, TX 79835. This address does not seem to exist.

4. A DNS lookup shows that the IP of wattsamp.net is 157.230.179.99. Shodan shows that this IP is located in New York and is associated with Digital Ocean.

5. Found robots.txt on wattsamp.net just from trying it out. I also found wattsamp.net/../assets and all the images on the site from insepct element.

6. An nmap scan of wattsamp.net shows 3 open ports: 22 (ssh), 80 (http), and 1337 (waste?). 

7. Shodan shows that the site is an Apache/2.4.29 Ubuntu server. It also shows that the ssh service is OpenSSH for Ubuntu, so the server is likely running Ubuntu.

8. Flags:
From inspect element on wattsamp.net: *CMSC389R-{html_h@x0r_lulz}
From wattsamp.net/robots.txt: *CMSC389R-{n0_indexing_pls}
From dnsdumpster of wattsamp.net: *CMSC389R-{Do_you-N0T_See_this}

### Part 2 (75 pts)

The stub.py script automates the process of attempting logging in to ejnorman84's account. First, it establishes a connection with 157.230.179.99 port 1337 and waits for a response (the captcha). The solve_captcha method takes the socket and receives the captcha, splits it up, and evaluates the math, sending back the result. Sometimes, the recv() call comes before the server sends the full captcha, but not often enough to warrant a longer sleep, so if it fails, I just try again with a different array index. After solving the captcha, I send the username and current password and wait for the response. I didn't know the "pass" message ahead of time, so I just counted anything that's not "Fail" as a possible success. Sometimes, the server responds a little slowly, so the "Password:" prompt doesn't arrive until right before the "Fail" response, which triggers as a possible success. Finally, I used python's multiprocessing to speed up the process. I could've waited until the map returned to inspect the responses, but I didn't want to wait for all 14 million guesses, so I just kept an eye on the output until I saw "Success!" for hello1. My only concern was that the username wasn't ejnorman84, so if I somehow got through all 14 million passwords in rockyou without a success, I would've tried ejnorman and ejnoman.

Once I was in the shell, I just looked around, figured the best place to look was where Eric's personal data would be stored in the "/home" directory, and the flag was there!

Flag! CMSC389R-{!enough_nrg_4_a_str0ng_Pa$$wrd}
