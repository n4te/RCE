class Keygen():

    __login      = None
    __serial_key = None

    def __init__ (self, login):
        self.set_login(login)

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

    def login_routine (self):
        raise NotImplementedError

    def serial_key_routine(self):
        raise NotImplementedError

    def check_routine(self):
        raise NotImplementedError

    def generate_key(self):
        raise NotImplementedError
