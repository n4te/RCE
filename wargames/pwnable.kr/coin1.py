'''
Description:

    Mommy, I wanna play a game!
    (if your network response time is too slow, try nc 0 9007 inside pwnable.kr server)

    Running at : nc pwnable.kr 9007

Solution

Solver:
'''

from pwn import *
from time import sleep

user   = 'fd'
passwd = 'guest'
host   = 'pwnable.kr'
port   = 2222

coin1 = '''
cd /tmp; echo '
from socket import socket, AF_INET, SOCK_STREAM
from time   import sleep

host = "localhost"
port = 9007

def get_nc(data):
   return [int(i.split("=")[1], 10) for i in data.rstrip().split(" ")]

def send_data_and_check_result(send_data):
    global s
    s.send(send_data)
    data = s.recv(1024)
    data = data.rstrip()
    number = int(data, 10)
    a = str(number)[-1]
    if a == "9":
        return True
    return False

s = socket(AF_INET, SOCK_STREAM)
s.connect((host, port))
print s.recv(2048)
sleep(0.1)
data = s.recv(1024)
print data

print get_nc(data)

def phase1(array):
    global c
    while c:
        data = " ".join([str(i) for i in array[0:(len(array)/2)]]) + "\\n"
        if send_data_and_check_result(data):
            array = array[0:(len(array)/2)]
        else:
            array = array[len(array)/2:]
        if len(array) <= c:
            break
        c -= 1
    return array

def phase2(array):
    for i in array:
        s.send(str(i) + "\\n")
        sleep(0.1)
        data = s.recv(1024)
        if data.find("Correct!") != -1:
            break
        if data == "9\\n":
            while True:
                s.send(str(i) + "\\n")
                sleep(0.1)
                data = s.recv(1024)
                if data.find("Congrats!") != -1:
                    print data
                if data.find("Correct!") != -1:
                    return data
    return data

b = 100
while b: 
    n, c = get_nc(data)
    array = range(0, n)
    array = phase1(array)
    result = phase2(array)
    data = result[result.find("N="):]
    b -= 1
s.close()
' > coin1.py; python coin1.py > coin1.log; cat coin1.log;
'''

s = ssh(user, host, port, passwd)
flag, status = s.run_to_end(coin1)
print flag
s.close()

'''
Log:

[+] Connecting to pwnable.kr on port 2222: Done

---------------------------------------------------
-              Shall we play a game?              -
---------------------------------------------------

You have given some gold coins in your hand
however, there is one counterfeit coin among them
counterfeit coin looks exactly same as real coin
however, its weight is different from real one
real coin weighs 10, counterfeit coin weighes 9
help me to find the counterfeit coin with a scale
if you find 100 counterfeit coins, you will get reward :)
FYI, you have 30 seconds.

- How to play - 
1. you get a number of coins (N) and number of chances (C)
2. then you specify a set of index numbers of coins to be weighed
3. you get the weight information
4. 2~3 repeats C time, then you give the answer

- Example -
[Server] N=4 C=2     # find counterfeit among 4 coins with 2 trial
[Client] 0 1         # weigh first and second coin
[Server] 20            # scale result : 20
[Client] 3            # weigh fourth coin
[Server] 10            # scale result : 10
[Client] 2             # counterfeit coin is third!
[Server] Correct!

- Ready? starting in 3 sec... -


N=997 C=10

[997, 10]
Correct! (99)
Congrats! get your flag
b1NaRy_S34rch1nG_1s_3asy_p3asy
'''
