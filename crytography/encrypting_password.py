import os
from cryptography.fernet import Fernet



class PassEncrypt:

	def __init__(self,password_string):
		self.key = b''
		self.password_string = password_string
		self.encoded_password_string = b''
		self.encrypted_password_string = b''
		self.key_reader_func_flag = 0 # to check if function was called or not



	def key_reader(self):
		key_file_loc_flag =0
		key_extension_flag = 0
		while key_file_loc_flag == 0 and key_extension_flag ==0:
			key_file_loc = input("Enter Location of key : ").strip(' "" ')
			print("Entered Key file location is : {}".format( key_file_loc ))

			if(os.path.exists(key_file_loc)):
				print("test : ", key_file_loc[-3:])
				if key_file_loc[-3:] == 'key':
					key_extension_flag = 1
					print("Key exists and looks valid\n proceeding further ....")

				else:
					print("Key Valid but does not looks in correct format")

		#reading key
		with open(key_file_loc,'rb') as fp:
			self.key = fp.read()


		self.key_reader_func_flag = 1 #stating that the function was called
		


# Takes Password string as an argument, Encodes it , Encrypts using key and returns encrypted password byte string
	def encryptor(self):
		if not self.key_reader_func_flag == 1:
			print("kindly call key_reader function before calling encryptor function  ")

		else :
			self.encoded_password_string = self.password_string.encode()
			fernet_obj = Fernet(self.key)
			self.encrypted_password_string = fernet_obj.encrypt(self.encoded_password_string)


		return self.encrypted_password_string #byte string



if __name__ == "__main__":
	e1 = PassEncrypt("Password")
	e1.key_reader()
	print( e1.encryptor() )
