'''
Description:

    I have a binary that has a lot information inside heap.
    How fast can you reverse-engineer this?
    (hint: see the information inside EAX,EBX when 0x403E65 is executed)

    download: http://pwnable.kr/bin/codemap.exe
    
    ssh codemap@pwnable.kr -p2222 (pw:guest)

Solution:

    from pydbg         import *
    from pydbg.defines import *
    import pefile
    
    file_name  = 'codemap.exe'
    breakpoint = 0x00913E65

    def get_eax_ebx(dbg):
        global result
        result[dbg.context.Eax] = dbg.get_ascii_string(dbg.read(dbg.context.Ebx, 16))
        return DBG_CONTINUE

    result = {}
    dbg = pydbg()
    dbg.load(file_name)
    dbg.bp_set(breakpoint, handler=get_eax_ebx)
    dbg.run()
    
    print
    for key in sorted(result.keys())[::-1][1:3]:
        print result[key]
    
    # python.exe parser.py
    # I will make 1000 heap chunks with random size
    # each heap chunk has a random string
    # press enter to start the memory allocation
    # 3
    # the allcated memory size of biggest chunk is 99879 byte
    # the string inside that chunk is X12nM7yCJcu0x5u
    # log in to pwnable.kr and anwer some question to get flag.
    #
    # roKBkoIZGMUKrMb
    # 2ckbnDUabcsMA2s

Solver:
'''

from pwn import *

user    = 'codemap'
passwd  = 'guest'
host    = 'pwnable.kr'
port    = 2222
command = ''

s = ssh(user, host, port, passwd)
s.interactive()
s.close()

'''
Log:

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
     
     codemap@ubuntu:~$ nc 0 9021
     What is the string inside 2nd biggest chunk? :
     roKBkoIZGMUKrMb
     Wait for 10 seconds to prevent brute-forcing...
     What is the string inside 3rd biggest chunk? :
     2ckbnDUabcsMA2s
     Wait for 10 seconds to prevent brute-forcing...
     Congratz! flag : select_eax_from_trace_order_by_eax_desc_limit_20
     codemap@ubuntu:~$ exit
     logout
     [*] Got EOF while reading in interactive
     [*] Closed SSH channel with pwnable.kr
     [*] Closed connection to 'pwnable.kr'
'''
