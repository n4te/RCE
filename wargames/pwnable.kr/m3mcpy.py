'''
Description:

    Are you tired of hacking?, take some rest here.
    Just help me out with my small experiment regarding memcpy performance. 
    after that, flag is yours.

    http://pwnable.kr/bin/memcpy.c

    ssh memcpy@pwnable.kr -p2222 (pw:guest)

Source of :
    // compiled with : gcc -o memcpy memcpy.c -m32 -lm
    #include <stdio.h>
    #include <string.h>
    #include <stdlib.h>
    #include <signal.h>
    #include <unistd.h>
    #include <sys/mman.h>
    #include <math.h>
    
    unsigned long long rdtsc(){
        asm("rdtsc");
    }

    char* slow_memcpy(char* dest, const char* src, size_t len){
        int i;
        for (i=0; i<len; i++) {
            dest[i] = src[i];
        }
        return dest;
    }

    char* fast_memcpy(char* dest, const char* src, size_t len){
        size_t i;
        // 64-byte block fast copy
        if(len >= 64){
            i = len / 64;
            len &= (64-1);
            while(i-- > 0){
                __asm__ __volatile__ (
                "movdqa (%0), %%xmm0\n"
                "movdqa 16(%0), %%xmm1\n"
                "movdqa 32(%0), %%xmm2\n"
                "movdqa 48(%0), %%xmm3\n"
                "movntps %%xmm0, (%1)\n"
                "movntps %%xmm1, 16(%1)\n"
                "movntps %%xmm2, 32(%1)\n"
                "movntps %%xmm3, 48(%1)\n"
                ::"r"(src),"r"(dest):"memory");
                dest += 64;
                src += 64;
            }
        }
        
        // byte-to-byte slow copy
        if(len) slow_memcpy(dest, src, len);
            return dest;
    }

    int main(void){
        setvbuf(stdout, 0, _IONBF, 0);
        setvbuf(stdin, 0, _IOLBF, 0);
        
        printf("Hey, I have a boring assignment for CS class.. :(\n");
        printf("The assignment is simple.\n");
        
        printf("-----------------------------------------------------\n");
        printf("- What is the best implementation of memcpy?        -\n");
        printf("- 1. implement your own slow/fast version of memcpy -\n");
        printf("- 2. compare them with various size of data         -\n");
        printf("- 3. conclude your experiment and submit report     -\n");
        printf("-----------------------------------------------------\n");
        
        printf("This time, just help me out with my experiment and get flag\n");
        printf("No fancy hacking, I promise :D\n");
        
        unsigned long long t1, t2;
        int e;
        char* src;
        char* dest;
        unsigned int low, high;
        unsigned int size;
        // allocate memory
        char* cache1 = mmap(0, 0x4000, 7, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
        char* cache2 = mmap(0, 0x4000, 7, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
        src = mmap(0, 0x2000, 7, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
        
        size_t sizes[10];
        int i=0;
        
        // setup experiment parameters
        for(e=4; e<14; e++){    // 2^13 = 8K
            low = pow(2,e-1);
            high = pow(2,e);
            printf("specify the memcpy amount between %d ~ %d : ", low, high);
            scanf("%d", &size);
            if( size < low || size > high ){
                printf("don't mess with the experiment.\n");
                exit(0);
            }
            sizes[i++] = size;
        }
        
        sleep(1);
        printf("ok, lets run the experiment with your configuration\n");
        sleep(1);
        
        // run experiment
        for(i=0; i<10; i++){
            size = sizes[i];
            printf("experiment %d : memcpy with buffer size %d\n", i+1, size);
            dest = malloc( size );
            
            memcpy(cache1, cache2, 0x4000);     // to eliminate cache effect
            t1 = rdtsc();
            slow_memcpy(dest, src, size);       // byte-to-byte memcpy
            t2 = rdtsc();
            printf("ellapsed CPU cycles for slow_memcpy : %llu\n", t2-t1);
            
            memcpy(cache1, cache2, 0x4000);     // to eliminate cache effect
            t1 = rdtsc();
            fast_memcpy(dest, src, size);       // block-to-block memcpy
            t2 = rdtsc();
            printf("ellapsed CPU cycles for fast_memcpy : %llu\n", t2-t1);
            printf("\n");
        }
        
        printf("thanks for helping my experiment!\n");
        printf("flag : ----- erased in this source code -----\n");
        return 0;
    }

Solution

Solver:
'''

from pwn import *

user    = 'memcpy'
passwd  = 'guest'
host    = 'pwnable.kr'
port    = 2222
command = '''
cd /tmp; echo "
from pwn  import *
from time import sleep
import sys

path = [8, 16, 37, 69, 133, 277, 517, 1029, 2053, 4096]
r = remote('localhost', 9022)
count = 0

for i in range(4, 14):
    back =  str(2 ** (i-1)) + ' ~ ' + str(2 ** i) + ' : '
    print r.recvuntil(back)
    sleep(0.3)
    r.sendline(str(path[count]))
    print 'send', path[count]
    count += 1
sleep(5)
print r.recvuntil('flag : ')
sleep(0.1)
print r.recv(1024)
r.close()
" > m3mcpy.py;
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

memcpy@ubuntu:~$ python /tmp/m3mcpy.py
[+] Opening connection to localhost on port 9022: Done
Hey, I have a boring assignment for CS class.. :(
The assignment is simple.
-----------------------------------------------------
- What is the best implementation of memcpy?        -
- 1. implement your own slow/fast version of memcpy -
- 2. compare them with various size of data         -
- 3. conclude your experiment and submit report     -
-----------------------------------------------------
This time, just help me out with my experiment and get flag
No fancy hacking, I promise :D
specify the memcpy amount between 8 ~ 16 : 
send 8
specify the memcpy amount between 16 ~ 32 : 
send 16
specify the memcpy amount between 32 ~ 64 : 
send 37
specify the memcpy amount between 64 ~ 128 : 
send 69
specify the memcpy amount between 128 ~ 256 : 
send 133
specify the memcpy amount between 256 ~ 512 : 
send 277
specify the memcpy amount between 512 ~ 1024 : 
send 517
specify the memcpy amount between 1024 ~ 2048 : 
send 1029
specify the memcpy amount between 2048 ~ 4096 : 
send 2053
specify the memcpy amount between 4096 ~ 8192 : 
send 4096

ok, lets run the experiment with your configuration

experiment 1 : memcpy with buffer size 8
ellapsed CPU cycles for slow_memcpy : 1386
ellapsed CPU cycles for fast_memcpy : 195

experiment 2 : memcpy with buffer size 16
ellapsed CPU cycles for slow_memcpy : 312
ellapsed CPU cycles for fast_memcpy : 276

experiment 3 : memcpy with buffer size 37
ellapsed CPU cycles for slow_memcpy : 603
ellapsed CPU cycles for fast_memcpy : 558

experiment 4 : memcpy with buffer size 69
ellapsed CPU cycles for slow_memcpy : 1020
ellapsed CPU cycles for fast_memcpy : 201

experiment 5 : memcpy with buffer size 133
ellapsed CPU cycles for slow_memcpy : 1884
ellapsed CPU cycles for fast_memcpy : 153

experiment 6 : memcpy with buffer size 277
ellapsed CPU cycles for slow_memcpy : 3819
ellapsed CPU cycles for fast_memcpy : 471

experiment 7 : memcpy with buffer size 517
ellapsed CPU cycles for slow_memcpy : 7032
ellapsed CPU cycles for fast_memcpy : 249

experiment 8 : memcpy with buffer size 1029
ellapsed CPU cycles for slow_memcpy : 13809
ellapsed CPU cycles for fast_memcpy : 381

experiment 9 : memcpy with buffer size 2053
ellapsed CPU cycles for slow_memcpy : 28248
ellapsed CPU cycles for fast_memcpy : 792

experiment 10 : memcpy with buffer size 4096
ellapsed CPU cycles for slow_memcpy : 56397
ellapsed CPU cycles for fast_memcpy : 1596

thanks for helping my experiment!
flag : 
1_w4nn4_br34K_th3_m3m0ry_4lignm3nt

[*] Closed connection to localhost port 9022
memcpy@ubuntu:~$ exit
logout
[*] Got EOF while reading in interactive
[*] Closed SSH channel with pwnable.kr
[*] Closed connection to 'pwnable.kr'
'''
