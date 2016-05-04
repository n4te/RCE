from keygen import Keygen
import sys

class CRACKME(Keygen):

    def login_routine(self):
        hash = 0
        login = self.get_login()
        if not login.isalpha():
            print('[*] Login is not alpha')
            exit()
        login = login.upper()
        for symbol in login:
            num = ord(symbol)
            hash += num
        hash ^= 0x5678
        return hash

    def serial_key_routine(self):
        hash = 0
        serial_key = self.get_serial_key()
        for symbol in serial_key:
            num = ord(symbol) - 0x30
            hash *= 0xA
            hash += num
        hash ^= 0x1234
        return hash
	
    def check_routine(self):
        hash_login = self.login_routine()
        hash_serial_key = self.serial_key_routine()
        result = hash_login == hash_serial_key
        self.print_key(result)

    def generate_key(self):
        hash_login = self.login_routine()
        serial_key = str(hash_login ^ 0x1234)
        self.set_serial_key(serial_key)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('[*] Use CRACKME.py login')
    else:
        login = sys.argv[1]
        crackme = CRACKME(login)
        crackme()
