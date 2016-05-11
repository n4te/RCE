'''
Description:

    Daddy told me about cool MD5 hash collision today.
    I wanna do something like that too!

    ssh col@pwnable.kr -p2222 (pw:guest)

Source of col.c:

    #include <stdio.h>
    #include <string.h>

    unsigned long hashcode = 0x21DD09EC;

    unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
            res += ip[i];
        }
        return res;
    }

    int main(int argc, char* argv[]){
        if(argc<2){
            printf("usage : %s [passcode]\n", argv[0]);
            return 0;
        }
        if(strlen(argv[1]) != 20){
            printf("passcode length should be 20 bytes\n");
            return 0;
        }
        if(hashcode == check_password( argv[1] )){
            system("/bin/cat flag");
            return 0;
        }
        else
            printf("wrong passcode.\n");
        return 0;
    }
                                                                                                                        
Solution

Solver:
'''

from pwn import *

user     = 'col'
passwd   = 'guest'
host     = 'pwnable.kr'
port     = 2222
passcode = '\x01\x01\x01\x01' * 4 + '\xe8\x05\xd9\x1d'
command  = './col ' + passcode

s = ssh(user, host, port, passwd)
flag, status = s.run_to_end(command)
print '[+] Flag:', flag.rstrip()
s.close()

'''
Log:

[+] Connecting to pwnable.kr on port 2222: Done
[+] Flag: daddy! I just managed to create a hash collision :)
[*] Closed connection to 'pwnable.kr'
'''
