import os
from cryptography.fernet import Fernet 


class Generator:
	def __init__(self):
		self.generated_key = b''
		self.filepath = ''
		self.filename = 'key.key'

#generates key and saves into file, returns file location
	def generator(self):

		self.generated_key =Fernet.generate_key()

		with open(self.filename,'wb') as fp: #creating new file with extension .key and opening in write mode
			fp.write(self.generated_key)
		self.filepath = os.path.join ( os.getcwd(), "key.key")
		
		return self.filepath






if __name__ == "__main__":
	g1 = Generator()
	filepath = g1.generator()
	print("Key location is : {}".format( filepath ))

