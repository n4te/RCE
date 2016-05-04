class Keygen():

    __login      = None
    __serial_key = None
    __debug      = None

    def __init__ (self, login, debug=False):
        self.set_login(login)
        self.set_debug(debug)

    def __call__(self):
        self.generate_key()
        self.check_routine()

    def set_login(self, login):
        self.__login = login

    def get_login(self):
        return self.__login

    def set_serial_key(self, serial_key):
        self.__serial_key = serial_key

    def get_serial_key(self):
        return self.__serial_key

    def set_debug(self, debug):
        self.__debug = debug

    def is_debug(self):
        return self.__debug

    def dprint(self, message):
        if self.is_debug():
            print('[D] {}'.format(message))

    def print_key(self, flag):
        if flag:
            print('[+] Serial key: {}'.format(self.get_serial_key()))
        else:
            print('[-] WTF, serial key is bad')

    def login_routine(self):
        raise NotImplementedError

    def serial_key_routine(self):
        raise NotImplementedError

    def check_routine(self):
        raise NotImplementedError

    def generate_key(self):
        raise NotImplementedError
