#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "crypto.h"
#include "common.h"

#define LEDGER_FILE "ledger.bin"
#define PERMISSIONS (S_IRUSR | S_IWUSR)

#define MAX_KEY 65535

typedef union key
{
  unsigned short int num;
  unsigned char bytes[2];
} Key;

void generate_string(char *, size_t);

int main(int argc, char **argv)
{
  Key key;
  char user_input[17], *key_hash, *b_key_hash;
  int i, fd;
  struct stat st;

  // check if ledger exists, fail if not
  if (stat(LEDGER_FILE, &st) != 0) {
    die("ledger does not exist");
  } else {
    fd = open(LEDGER_FILE, O_RDONLY, PERMISSIONS);
    read(fd, key_hash, 16);

    key.num = -1;

    do {
      key.num++;
      b_key_hash = md5_hash(key.bytes, 2);
    } while (key.num <= MAX_KEY && memcmp(b_key_hash, key_hash, 16));

    // now, we need to brute force the user input needed to generate that key
    // can't think of a better way than just generate random ascii strings until something matches
    do {
      generate_string(user_input, 16);
      key_hash = md5_hash(user_input, 16);
    } while (memcmp(key_hash, key.bytes, 2)); // loop until we have a match

    printf("%s", user_input);
  }

  return 0;
}

void generate_string(char *buf, size_t size)
{
  const char chars[] = "abcdefghijklmnopqrstuvwxyz";
  buf[size] = '\0';
  while (size--) {
    buf[size] = chars[rand() % (int) (sizeof(chars) -1)];
  }
}
