'''

Description:
    
    Daddy, teach me how to use random value in programming! 
    
    ssh random@pwnable.kr -p2222 (pw:guest)

Source of random.c:
    
    #include <stdio.h>
    int main(){
        unsigned int random;
        random = rand();    // random value!
        unsigned int key=0;
        scanf("%d", &key);
        if( (key ^ random) == 0xdeadbeef ){
            printf("Good!\n");
            system("/bin/cat flag");
            return 0;
        }
        printf("Wrong, maybe you should try 2^32 cases.\n");
        return 0;
    }
Solution

Solver:
'''

from ctypes import *
from pwn import *

libc = cdll.LoadLibrary('libc.so.6')
libc.srand(1)
random = libc.rand()
solution = str(random ^ 0xdeadbeef)

user    = 'random'
passwd  = 'guest'
host    = 'pwnable.kr'
port    = 2222
command = 'echo "{}" | ./random'.format(solution)

s = ssh(user, host, port, passwd)
flag, status = s.run_to_end(command)
print '[+] Flag:', flag
s.close()

'''
Log:

[+] Connecting to pwnable.kr on port 2222: Done
[+] Flag: Mommy, I thought libc random is unpredictable...
Good!
[*] Closed connection to 'pwnable.kr'
'''
