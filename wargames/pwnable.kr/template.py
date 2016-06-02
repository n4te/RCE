'''
Description:
    
Source of :

Solution

Solver:
'''

from pwn import *

user    = ''
passwd  = 'guest'
host    = 'pwnable.kr'
port    = 2222
command = ''

s = ssh(user, host, port, passwd)
flag, status = s.run_to_end(command)
print flag
s.close()

'''
Log:


'''
