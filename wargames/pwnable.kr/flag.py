'''
Description:

    Papa brought me a packed present! let's open it.

    Download : http://pwnable.kr/bin/flag

    This is reversing task. all you need is binary

Solution

Solver:
'''

import subprocess

gdb_script = 'b strcpy\nr\nx/s $rsi\nq\n'
with open('script', 'w') as h_file:
    h_file.write(gdb_script)

command='gdb --nh ./flag --command=script'
subprocess.check_output('wget http://pwnable.kr/bin/flag && upx -d ./flag && chmod +x ./flag', shell=True)
r = subprocess.check_output(command, shell=True)
start = r.find('UPX')
end   = r.find(':)"') + 2
flag = r[start:end]
print '[+] Flag:', flag
subprocess.check_output('rm flag script',shell=True)

'''
Log:

Resolving pwnable.kr (pwnable.kr)... 143.248.249.64
Connecting to pwnable.kr (pwnable.kr)|143.248.249.64|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 335288 (327K)
Saving to: ‘flag’
flag                100%[=====================>] 327,43K   209KB/s   in 1,6s   
2016-05-12 16:57:06 (209 KB/s) - ‘flag’ saved [335288/335288]
[+] Flag: UPX...? sounds like a delivery service :)
'''
