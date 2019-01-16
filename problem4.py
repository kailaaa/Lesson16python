password = input('What is the password? ')

while password not in ['Open Sesame']:
	password = input('Passwod is incorrect, try again. ')

print('Password is correct, welcome!')