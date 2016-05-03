class KeyGen():
	'''
	Base class for keygen
	'''
	__login               = None
	__login_routine       = None
	__serial_key          = None
	__serial_key_routine  = None
	__check_routine       = None
	__generate_serial_key = None
	
	def __init__ (self, login, serial_key):
		self.setLogin(login)
		self.setSerialKey(serial_key)
	
	def setLogin(self, login):
		self.__login = login
	
	def getLogin(self):
		return self.__login
	
	def setLoginRoutine(self, login_routine):
		self.__login_routine = login_routine
	
	def getLoginRoutine(self):
		return self.__login_routine
	
	def setSerialKey(self, serial_key):
		self.__serial_key = serial_key
	
	def getSerialKey(self):
		return self.__serial_key
	
	def setSerialKeyRoutine(self, serial_key_routine):
		self.__serial_key_routine = serial_key_routine
	
	def getSerialKeyRoutine(self):
		return self.__serial_key_routine
	
	def setCheckRoutine(self, check_routine):
		self.__check_routine = check_routine
	
	def getCheckRoutine(self):
		return self.__check_routine
	
	def setGenerateSerialKey(self, generate_serial_key):
		self.__generate_serial_key = generate_serial_key
	
	def getGenerateSerialKey(self):
		return self.__generate_serial_key
	
	def loginRoutine (self):
		raise NotImplementedError
	
	def serialKeyRoutine(self):
		raise NotImplementedError
	
	def checkRoutine(self):
		raise NotImplementedError
	
	def generateSerialKey(self):
		raise NotImplementedError