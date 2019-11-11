# Writeup 9 - Forensics II

Name: Charlie Schneider 
Section: 0101 

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charles Schneider 


## Assignment details

### Part 1 (45 Pts)
1. The IP address being attacked is 142.93.136.81, the IP for 1337bank.money.

2. Based on the large number of empty TCP requests sent to the target on a number of ports, it looks like the attackers used nmap to scan the ports of the victim machine. The attackers are also able to simply log in to the FTP service, so they must have obtained the victim's credentials at some point.

3. The nmap scan, as well as the login, download, and upload, are all from 159.203.113.181, which GeoIP says is located in Clifton, New Jersey.

4. The attackers are using port 21 to steal files. This port is commonly used for the FTP protocol.

5. The attackers stole the file `find_me.jpeg`, which is a valid jpeg file that does not seem to contain any other information.

6. The attackers left the file `greetz.fpff` on the server, which appears to be a binary file in a strange format.

7. The nmap scan showed that port 21 was open, which the attackers likely used to guess that the server was running the vulnerable FTP service. Setting up a firewall that shows port 21 as closed or filtered might help prevent intrusion. The firewall could also be used to whitelist only specific IPs to use the FTP service through port 21. Additionally, some automated system could have been set up to recognize the massive scan from the attacker IP and then block further communication. 

### Part 2 (55 Pts)

1. See `carver.py`.

2. The results of running `$ python carver.py greetz.fpff` are included in this directory.
i. The file was generated on March 27, 2019 at 12:15AM.
ii The file was authored by fl1nch.
iii. 
<pre><code>Section 1 
    Section Type: 1 (SECTION_ASCII) 
    Section Length: 24 
    Section Value: Hey you, keep looking :) 
Section 2 
    Section Type: 6 (SECTION_COORD) 
    Section Length: 16
    Section Value: (52.336035, 4.880673) 
Section 3 
    Section Type: 8 (SECTION_PNG) 
    Section Length: 202776 
    Section Value: Data written to file 88.png 
Section 4 
    Section Type: 1 (SECTION_ASCII) 
    Section Length: 44 
    Section Value: }R983CSMC_perg_tndid_u0y_yllufep0h{-R983CSMC 
Section 5 
    Section Type: 1 (SECTION_ASCII) 
    Section Length: 80 
    Section Value: Q01TQzM4OVIte2hleV9oM3lfeTBVX3lvdV9JX2RvbnRfbGlrZV95b3VyX2Jhc2U2NF9lbmNvZGluZ30=</code></pre>
    
iv. I found 3 three flags: 

First, in the file `88.png`, which was extracted from `greetz.fpff`, has the flag CMSC389R-{w31c0me_b@ck_fr0m_spr1ng_br3ak}. 

The ASCII text in Section 4 is just CMSC389R-{h0pefully_y0u_didnt_grep_CMSC389R} in reverse.  

The ASCII text in Section 5 looks like base64, and base64decoding it gave CMSC389R- {hey_h3y_y0U_you_I_dont_like_your_base64_encoding}.
