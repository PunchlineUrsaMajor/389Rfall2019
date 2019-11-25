# Writeup 1 - Web I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

Based on the comment provided, I assumed there would be some kind of SQL injection vulnerability. When I click on one of the exploits for sale, it shows that it's selected using `id=0`, so that must be the attack vector. I tested to see if -1 was a valid id, and it was not. So I tried entering `-1' OR '1'='1` as the id parameter, but it seems like there's something that detects attempted SQL injection. Remembering what was said in class, I tried replacing the OR with ||, and that worked (I guess it doesn't check for '='). So the final input was appending `-1'||'1'='1` to the URL, which displayed every entry in the database, including the flag, which is `CMSC389R-{y0u_ar3_th3_SQ1_ninj@}`.

### Part 2 (60 Pts)
Complete all 6 levels of:

[https://xss-game.appspot.com](https://xss-game.appspot.com)

Produce a writeup. We will not take off points for viewing the source code and/or viewing hints, but we strongly discourage reading online write-ups as that defeats the purpose of the homework.

Level 1: This level only needs you to open an alert in the provided browser. Anything entered in the search field is passed through http in the `query` parameter. So, all I needed to do was enter `<script>alert()</script>` into the search bar. 

Level 2: From the example post, it seems like you can use html tags within a message to add stuff like italics and colors. This means I can insert any html elements I want through the post field. So, I just added a button that, when clicked, causes an alert. The exact input was `<button type="button" onclick="alert()">XSS</button>`. Then, after posting, I can just click the button to trigger an alert.

Level 3: Looking at the html for the page, it looks like the page knows what image to show from whatever number follows the # in the URL. I tried just entering `"><script>alert()</script>` to end the img tag and inject the script, but it seems like whatever function replaces the number escapes any quotation marks. I tried using a single quote instead, which properly escaped the img tag and injected the script, so the final input was appending `'><script>alert()</script>` to the URL. 

Level 4: This level uses a similar function call to the last level, but now there is a field with which to enter the payload. The value passed to `startTimer()` is not inserted anywhere, so I need to break out of the `startTimer` call and insert the script. So, I need to end the string with ', end the function with ), end the line with ;, then insert the `alert('')`. Except, there is still the ') after the string, so I need to take the last two characters off the alert. So the final input is `');alert('`. 

Level 5: In this level, I can follow a series of links through the "signup" procedure. On the "signup" page, the "next" parameter decides where the "Next >>" link refers to. So, if I can manipulate the link, I might be able to inject a script. I tried a lot of various escaping sequences to break out of the anchor tag, but nothing was working. I thought maybe I could link to a page that somehow injects javascript, but in searching for that, I found a way to execute javascript through anchor tags using the `javascript:` prefix. So, I just appended `next=javascript:alert()` to the URL, clicked the link, and caused the alert. 

Level 6: In this level, the application seems to load whatever file comes after frame# in the URL, so all I need to do is point it to some external file that has an `alert()` call. I tried hosting it off github, but it did not work for some reason. So, I just put up a paste on pastebin that says `alert();`, and appended that link to the URL. So the input was `https://pastebin.com/raw/zyf0XtdU`. The last hurdle was that the site won't load anything with an "http" in it, as a protection against the exact attack I'm attempting. I tried using encoded html to get past it, but it didn't seem to work. I tried taking the error a little more literally, and changed the "https" to "HTTPS" and it worked. Whatever checks the file reference is case-sensitive, but URLs are not. So the final input was `HTTPS://pastebin.com/raw/zyf0XtdU`.


### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
