# Writeup 1 - Ethics

Name: Charlie Schneider
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Charles Schneider

## Assignment Writeup

### Part 1 (25 pts)

This was done via the ELMS assignment.

### Part 2 (75 pts)

As the auditor of the software, I should tell whoever employed me to check it.
Telling my employer or boss allows them to make the decisions that will lead to the vulnerabilities being fixed. Using the information I found during the audit, we can hopefully fix the issues as fast 
as possible, minimizing how long drivers are in danger with the current exploitable ECU firmware. The patches need to be done well and thoroughly examined for new issues so we do not accidentally 
introduce any more exploitable vulnerabilities.
Making my findings public could help people understand the danger of driving cars with the current ECU, but it would also open up those people to be targeted by malicious actors using the exploits I 
reported. Even if I do not publish the exact vulnerabilities, simply saying "this ECU version has several serious vulnerabilities" could lead to tons of malicious actors suddenly fixing their sights on 
something they weren't paying attention to either. The danger could be mitigated by issuing some sort of recall on cars with this ECU version, but that seems completely infeasible, as I'm assuming this 
problem affects most cars recently produced by a large manufacturer, so even if a recall was issued, there would be no way to properly replace everyone's cars for at least six months.

If my company is unwilling to take action on the ECU software, that's when it becomes my responsibility to inform a trusted consumer service. If the vulnerabilities are allowed to sit there, eventually, 
someone else will find one or more of them, and we will not have a patch ready. Now, the consumers are in danger, and we are not doing anything to mitigate that. If disclosing the vulnerabilities to the 
public causes damage to this company's reputation or value, the loss does not outweigh the potential danger of doing nothing.
I could try to work on patches myself, but considering the complexity of the vulnerabilities, there's no way I could do it myself, nor could I feasibly put together and pay a team of 20 trusted 
developers to fix it. 

If I do nothing, I am partially responsible for any harm that comes from it. As the person who discovered the vulnerabilities, I am in the position to most effectively fix the vulnerabilities by 
reporting my findings. Though I would not be the person actually exploiting the vulnerabilities, my inaction would allow the exploits to occur, so some responsibility falls on me.
