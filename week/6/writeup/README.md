# Writeup 6 - Binaries I

Name: Charlie Schneider
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charles Schneider

## Assignment Writeup

### Part 1 (50 pts)

Flag: CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)

First, I opened crackme in BinaryNinja and looked at the top level main() function. Most of the first block of main() is spent setting pointers, but the important part is that argv, the list of argument strings, is saved to a local variable, and argc, the argument counter, is stored as well. Also, argc is compared to 1, and the code jumps based on whether argc is greater than 1. This told me that the binary is expecting at least 1 argument other than `./crackme`. If argc is greater than 1, check1 is eventually called with argv as an argument. Check 1 loads a string constant "Oh God" and compares that to the passed argv using strcmp, which returns 0 if the two strings are equal. The code jumps depending on the result of strcmp, so the two strings need to be equal, so "Oh God" needs to be passed on the command line. So, th input is `./crackme "Oh God"`.

The next check is check2, which loads the string constant "FOOBAR" and pushes it onto the stack before a call to getenv. From searching, getenv returns the value associated with the passed variable name in the current environment. So, this call returns the value of "FOOBAR" in the current environment, and this value is compared to 0, and the program continues if the value is not 0. The documentation shows that getenv returns NULL (0) if the variable does not exist, so the variable "FOOBAR" must exist. The binary also loads the constant "seye ym ", which is " my eyes" reversed. Later, the binary calls strlen on the value of "FOOBAR" and compares it to the constant 8, so it must be expecting FOOBAR to be a string with length 8, and "my eyes " is 8 characters long. I cannot set anything within the binary's environment, so I have to set FOOBAR within the bash environment with `export FOOBAR="my eyes "`, which unlocks the next check.

Check 3 pushes the string "sesame" onto the stack and calls open, which returns a file pointer to the start of a file called "sesame", so I know I need to create a file called "sesame" in the same directory as crackme. Next, it calls read on that file pointer, which fills a buffer with the contents of "sesame" and returns the number of bytes read. The binary tests of the return value is compared to 0xa (10), so I know the file needs to contain 10 bytes. The file is then closed and a counter is set to 9, and the binary starts a loop that checks if the counter is 0 at the top. This loop incrementally loads each byte of the string read from "sesame", and branches depending on the counter value. In each branch, the string byte is compared to a different hex value, which means each value corresponds to an ASCII character. The characters are 0x20, 0x74, 0x68, 0x65, 0x79, 0x20, 0x62, 0x75, 0x72, and 0x6e, which corresponds to the string " they burn". So, I write " they burn" to the file "sesame" with `echo " they burn" > sesame`.

So, the binary takes input from the command line, the environment, and files. The flag is constructed by several calls to `update_flag` which performs various operations on the bytes of a local variable that must represent the flag. Each passed "check" calls update_flag with a new set of arguments that form the correct flag format. This obfuscates the literal "flag" by pulling the data for the various ASCII characters from within the program instead of simply storing it where the flag could easily be found. Only the correct inputs will produce the correct flag.

The total correct input is `$ export FOOBAR=" my eyes"; echo " they burn" > sesame; ./crackme "Oh God"`.
