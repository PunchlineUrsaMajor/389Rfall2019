# Writeup 7 - Forensics I

Name: Charlie Schneider
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charles Schneider

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding [this](../image) file:

1. What kind of file is it? 

The file is a JPG file, according to the output from `file image`, though `binwalk image` shows that there is also a png file hidden inside the jpeg.

2. Where was this photo taken? Provide a city, state and the name of the building in your answer. 

Using the information from `exiftool image`, I found the latitude and longitude information on where the image was taken. I entered that information into Google Maps and found the location. This photo was taken in Chicago, Illinois, at the John Hancock Center.

3. When was this photo taken? Provide a timestamp in your answer. 

Using the same `exiftool image` output, I found that the image was originally taken on 8/22/2018 at 16:33:24 UTC, or 11:33:24AM CDT.

4. What kind of camera took this photo? 

This photo was taken on an Apple iPhone 8 back camera.

5. How high up was this photo taken? Provide an answer in meters. 

This photo was taken at 539.5 meters above sea level

6. Provide any found flags in this file in standard flag format. 

CMSC389R-{look_I_f0und_a_str1ng} - from running `strings image | grep CMSC`

CMSC389R-{abr@cadabra} - from running `binwalk --dd=".*" image` to extract all files and viewing the PNG output.
