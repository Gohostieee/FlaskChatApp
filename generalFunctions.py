from Crypto.Cipher import AES
from cryptography.fernet import Fernet

import json 
key=b'secret'
fernet = Fernet(key)
def passwdCheck(password):
	checks={
		"upper case":0,
		"lower case":0,
		"non-alphanumeric":0,
		"numbers":0,
		"8 characters":0
	}
	if not (password.isalnum()):
		checks['non-alphanumeric']=1
	if any(x.isdigit() for x in password):
		checks['numbers']=1
	if any(x.islower() for x in password):
		checks['lower case']=1
	if any(x.isupper() for x in password):
		checks['upper case']=1
	if len(password)>7:
		checks['8 characters']=1
	return checks
def encrypt(text):
	return fernet.encrypt(text.encode())
def decrypt(text):
	return fernet.decrypt(text).decode()
if __name__ == "__main__":
	kekw={"frame":"work","every":"day"}
	json_object = json.dumps(kekw, indent = 4) 
	kekw2=encrypt((json_object))
	print(typeof(kekw2))
	print(decrypt(kekw2))

