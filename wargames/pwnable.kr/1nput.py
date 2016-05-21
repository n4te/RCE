'''
Description:

    Mom? how can I pass my input to a computer program?

    ssh input@pwnable.kr -p2222 (pw:guest)

Source of input.c:

    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <sys/socket.h>
    #include <arpa/inet.h>

    int main(int argc, char* argv[], char* envp[]){
        printf("Welcome to pwnable.kr\n");
        printf("Let's see if you know how to give input to program\n");
        printf("Just give me correct inputs then you will get the flag :)\n");

        // argv
        if(argc != 100) return 0;
        if(strcmp(argv['A'],"\x00")) return 0;
        if(strcmp(argv['B'],"\x20\x0a\x0d")) return 0;
        printf("Stage 1 clear!\n"); 

        // stdio
        char buf[4];
        read(0, buf, 4);
        if(memcmp(buf, "\x00\x0a\x00\xff", 4)) return 0;
        read(2, buf, 4);
        if(memcmp(buf, "\x00\x0a\x02\xff", 4)) return 0;
        printf("Stage 2 clear!\n");

        // env
        if(strcmp("\xca\xfe\xba\xbe", getenv("\xde\xad\xbe\xef"))) return 0;
        printf("Stage 3 clear!\n");

        // file
        FILE* fp = fopen("\x0a", "r");
        if(!fp) return 0;
        if( fread(buf, 4, 1, fp)!=1 ) return 0;
        if( memcmp(buf, "\x00\x00\x00\x00", 4) ) return 0;
        fclose(fp);
        printf("Stage 4 clear!\n"); 

        // network
        int sd, cd;
        struct sockaddr_in saddr, caddr;
        sd = socket(AF_INET, SOCK_STREAM, 0);
        if(sd == -1){
            printf("socket error, tell admin\n");
            return 0;
        }
        saddr.sin_family = AF_INET;
        saddr.sin_addr.s_addr = INADDR_ANY;
        saddr.sin_port = htons( atoi(argv['C']) );
        if(bind(sd, (struct sockaddr*)&saddr, sizeof(saddr)) < 0){
            printf("bind error, use another port\n");
            return 1;
        }
        listen(sd, 1);
        int c = sizeof(struct sockaddr_in);
        cd = accept(sd, (struct sockaddr *)&caddr, (socklen_t*)&c);
        if(cd < 0){
            printf("accept error, tell admin\n");
            return 0;
        }
        if( recv(cd, buf, 4, 0) != 4 ) return 0;
        if(memcmp(buf, "\xde\xad\xbe\xef", 4)) return 0;
        printf("Stage 5 clear!\n");
    
        // here's your flag
        system("/bin/cat flag");    
        return 0;
    }

Solution

Solver:
'''

from pwn import *
from time import sleep

user   = 'input'
passwd = 'guest'
host   = 'pwnable.kr'
port   = 2222
bypass = '''
cd /tmp; echo '
#include <stdio.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>

    int main() {

        char* argv[101] = {[0 ... 99] = \"H\", NULL};
        argv[65] = \"\\x00\";
        argv[66] = \"\\x20\\x0a\\x0d\";
        argv[67] = \"1337\";

        int pipe_in[2], pipe_err[2];
        pipe(pipe_in);
        pipe(pipe_err);
        write(pipe_in[1], \"\\x00\\x0a\\x00\\xff\", 4);
        write(pipe_err[1], \"\\x00\\x0a\\x02\\xff\", 4);
        dup2(pipe_in[0], 0);
        dup2(pipe_err[0], 2);

        char* envp[2] = {\"\\xde\\xad\\xbe\\xef=\\xca\\xfe\\xba\\xbe\", NULL};

        FILE* f = fopen(\"\\x0a\", \"wb\");
        fwrite(\"\\x00\\x00\\x00\\x00\", 4, 1, f);
        fclose(f);

        if (fork() != 0) {
            execve(\"/home/input/input\", argv, envp);
        } else {
            int client;
            client = socket(AF_INET, SOCK_STREAM, 0);
            struct sockaddr_in server;
            server.sin_addr.s_addr = inet_addr(\"127.0.0.1\");
            server.sin_family = AF_INET;
            server.sin_port = htons(atoi(argv[67]));
            connect(client, (struct sockaddr *)&server, sizeof(server));
            write(client, \"\\xde\\xad\\xbe\\xef\", 4);
            close(client);
        }
        return 0;
    }
' > bypass.c; gcc bypass.c -o bypass; chmod +x bypass; ln /home/input/flag flag; ./bypass > bypass.log;
''' 

s = ssh(user, host, port, passwd)
s.run_to_end(bypass)
sleep(5)
flag, status = s.run_to_end('cat /tmp/bypass.log;')
print '[+] Flag:', flag
s.close()

'''
Log:
[+] Connecting to pwnable.kr on port 2222: Done
ln: failed to create hard link `flag': File exists

1
[+] Flag: Mommy! I learned how to pass various input in Linux :)
Welcome to pwnable.kr
Let's see if you know how to give input to program
Just give me correct inputs then you will get the flag :)
Stage 1 clear!
Stage 2 clear!
Stage 3 clear!
Stage 4 clear!
Stage 5 clear!
'''
