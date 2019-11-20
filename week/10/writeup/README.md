# Writeup 10 - Crypto I

Name: Charlie Schneider
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Charles Schneider


## Assignment details

### Part 1 (45 Pts)

1. The first 16 bytes of the ledger are the hash of the key used to encrypt the ledger. The next 16 bytes are the hash of the ciphertext. The next 16 bytes are the initialization vector that is randomly generated the first time the ledger is made. The remaining bytes (file size - 48) is the ciphertext of the contents of the ledger.

2. The ledger uses md5 to hash the user input (making the key), the key, and the ciphertext. After it first hashes the user input, it also sets all but the first two bytes to zero, limiting the hash space. Then, it hashes the key to create the key's hash to store in the file. md5 is considered weak and prone to collisions, and since the key is already truncated, there are bound to be more collisions based on the user input. It also uses aes128 to encrypt the ledger information, which is considered weak due to a small ciphertext space compared to modern computing standards. The initialization vector, however, is created with openssl's RAND_bytes(), which produces cryptographically-strong pseudorandom bytes.

3. Without decrypting ledger.bin, you can find the hash of the key used to encrypt the ciphertext, the initialization vector in plaintext, and the hash of the ciphertext. Since you know the size of the those fields, you can also figure out the size of the ciphertext.

4. The ledger ensures confidentiality by encryting the ledger contents before they are ever written to file. The encryption key is based on the argument the user provides to the ledger program. The key itself is the first two bytes of the md5 hash of the user input.

5. Integrity is ensured by checking if the hash of the ciphertext matches the hash stored in the file. This seems faulty, as it uses md5, which is a weaker hashing algorithm, and also, someone could modify the ciphertext, hash it, and overwrite the original ciphertext hash with the new hash, and there would be no way of verifying the integrity of the ciphertext.

6. Authenticity is ensured by checking if the hash of the provided key matches the hash of the key stored in the file. Again, this uses md5 (plus truncation), so the total key space is relatively small and prone to collisions.

7. The initialization vector is first generated when the ledger is first created. It is generated using openssl's RAND_bytes() method, which generates cryptographically-secure pseudorandom bytes. It is stored in plaintext in the ledger, which is not an issue since the IV simply needs to be random and unique. The IV is generated and stored in a secure manner.

### Part 2 (45 Pts)

1. Run ./ledger `writeup/crack`. It starts by reading in the first 16 bytes of ledger.bin, which is the hash of the key. Since I know that the key is only two bytes, which is only 65536 possible values, I can just hash every possible combination of two bytes until a hash matches the hashed key. Once I have the key, I need to find some string such that the first two bytes of the hash of that string are the key. There should be a lot of strings that match that, so I just generate random strings until the hash of the string has the right first bytes. Generally, this does not take long. Once we have a string, print that so it gets passed to the ledger file. The string it finds is most likely not the original password, but it works due to hashing collisions.

2. CMSC389R-{k3y5p4c3_2_sm411}

### Part 3 (10 Pts)

I believe the ideal balance is entirely towards Kerckoff's principle. Systems like RSA are secure because it is mathematically hard to break them, despite knowing exactly how the system works. At that point, any added layer of obscurity just adds to the security. If the only information that needs to be kept secret is a private key, then it is easier to prevent an attacker from finding that essential information. In contrast, a system that relies on obscurity requires much more information to be kept secret. Someone, somewhere, must have the obscured information, and that information is more complex that just a simple key. In the case of this assignment, the obscurity makes the system human-proof, meaning that I could not sit down and figure out the right input in a feasible amount of time, but computationally, there is nothing mathematically hard about the system. Given enough time to figure out the secret operations, a computer can then quickly crack the system.
Now, making everything public yet secure still has disadvantages. When the enemy knows the system, the enemy knows how to spoof the system or may even develop an attack on the system. For systems like ElGamal, there is an algorithm for recovering the private key that runs in square-root time on the size of the public key prime (Baby-Step Giant-Step). If an attacker can tell what system you are using, they may be able to engineer an attack, though it may take some time. However, there are ways to guarantee authenticity and integrity even with a system where everything is public, such as signatures and MAC. As for attacks like Baby-Step Giant-Step, there is not much to do besides continually increase key sizes to stay ahead of modern computers. In the end, I believe that security through obscurity is not enough to guarantee security, and that a good secure system should be hard to crack even if its operation is public knowledge. That said, obscurity can still add security to such a system, but only until someone figures the operations out.