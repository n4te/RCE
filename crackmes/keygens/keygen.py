import logging

class Keygen():

    __login      = None
    __serial_key = None
    __debug      = None
    __logger     = None

    def __init__ (self, login, debug=False):
        self.set_login(login)
        self.set_debug(debug)
        self.set_logger()

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

    def set_logger(self):
        logging.basicConfig(format="[%(levelname)s] %(message)s", level=logging.DEBUG)
        self.__logger = logging.getLogger()

    def logger(self, message):
        if self.is_debug():
            self.__logger.debug(message)

    def login_routine(self):
        raise NotImplementedError

    def serial_key_routine(self):
        raise NotImplementedError

    def check_routine(self):
        raise NotImplementedError

    def generate_key(self):
        raise NotImplementedError
