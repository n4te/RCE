##What do we have ?
```sh
$ file youPecks
youPecks: PE32 executable (console) Intel 80386, for MS Windows, UPX compressed
```

##The OEP is found. Let's look around
```asm
00DF3A8A     E8 94040000      CALL youPecks.00DF3F23
00DF3A8F    ^E9 B3FDFFFF      JMP youPecks.00DF3847
00DF3A94     6A 14            PUSH 14
00DF3A96     68 E85ADF00      PUSH youPecks.00DF5AE8
00DF3A9B     E8 D0010000      CALL youPecks.00DF3C70
...
```
##The program take a single argument
```asm
...
00BD14EE   837D 08 02       CMP DWORD PTR SS:[EBP+8],2
00BD14F2   74 6C            JE SHORT youPecks.00BD1560
...
00BD1560   8B47 04          MOV EAX,DWORD PTR DS:[EDI+4]
00BD1563   50               PUSH EAX
00BD1564   FF15 F450BD00    CALL DWORD PTR DS:[BD50F4]               ; MSVCR100.atoi
...
```
##Wrote a script for brute force the argument
```py
import os, sys
for i in xrange(0, 15):
    os.system('C:\\Users\\user\\Downloads\\youPecks.exe' + ' ' + str(i))
```
##Brute force the argument
```sh
$ python.exe brute.py

2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
2 + 2 = 4
Uhr1thm3tic@flare-on.com
2 + 2 = 4
```
##The email is found

Email: Uhr1thm3tic@flare-on.com

## Got message

You make it look easy. Are you some sort of wizard? Our cyberspace commandos captured some network traffic and a program they think may be responsible but the turbo hackers nuked everything else. Find the key, the password to the zip archive is "flare" once again.

We are counting on you!

-FLARE
