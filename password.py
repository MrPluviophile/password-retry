password = 'a123456'
guesscount = 0
while guesscount <= 2:
	guess = input('Please input the password: ')
	if guess == password:
		print('Login successful')
		break
	else:
		guesscount = guesscount + 1
		print('Incorrect Password, you have', 3 - guesscount, 'chances.')
if guesscount == 3:
	print('Attempt Limit Exceeded, Fail to Login')
raise SystemExit