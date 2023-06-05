password = 'a123456'
guesscount = 0
while guesscount <= 2:
	guess = input('Please input the password: ')
	if guess == password:
		break
	else:
		guesscount = guesscount + 1
		if guesscount == 3:
			print('Attempt Limit Exceeded, Fail to Login')
			break
		print('Incorrect Password, you have', 3 - guesscount, 'chances.')
if guesscount != 3:
	print('Login successful')
raise SystemExit