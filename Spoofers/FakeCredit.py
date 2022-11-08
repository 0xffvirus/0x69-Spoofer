def CFake():
	import random
	from faker import Faker
	from termcolor import colored
	only_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	forma = "{}{}{}{} {}{}{}{} {}{}{}{} {}{}{}{}"  # placeholders for digits
	fake = Faker()
	num = int(input("Count [0-100]: ")) # Number of Credit Cards
	if num <= 100: # Number of Credits should be equal of less than 100
		print("==================================")
		for i in range(num):
			Cred = fake.credit_card_number(card_type='visa') # Generate Visa Credit Card [ Can be changed to mastercard etc. ]
			f = forma.format(*Cred) # reformat credit card numbers to forma xxxx xxxx xxxx xxxx
			ccvgen = random.choice(only_numbers) + random.choice(only_numbers) + random.choice(only_numbers) # ccv generator
			print(colored("Credit Card:", 'cyan'), f"{f} | VISA")
			print(colored("CCV:", 'cyan'), ccvgen)
			print(colored("Expire Date:", 'cyan'), fake.credit_card_expire(end='+6y')) # Expire Date
			print("==================================")
	else:
		print("Over 100+ Credit Cards .. Please try again") # User entered a number above 100+
	input(colored("Press Enter to exit ...", 'red'))