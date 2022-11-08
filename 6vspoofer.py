import os
from Spoofers.eSpoof import espof
from Spoofers.FakeCredit import CFake # Fake Credit Card
from Spoofers.FakeAdd import Fadd # Fake Address
from Spoofers.IpFake import FakeIp # Fake ipv4, ipv6
from termcolor import colored # Coloring Text
os.system("color")
def Options():
	opt = int(input("0x69 > ")) ## User input option
	if opt == 1:
		espof()
	elif opt == 2:
		CFake()
	elif opt == 3:
		Fadd()
	elif opt == 4:
		FakeIp()
print(colored("""
 ██████╗ ██╗  ██╗ ██████╗ █████╗ 
██╔═████╗╚██╗██╔╝██╔════╝██╔══██╗
██║██╔██║ ╚███╔╝ ███████╗╚██████║
████╔╝██║ ██╔██╗ ██╔═══██╗╚═══██║
╚██████╔╝██╔╝ ██╗╚██████╔╝█████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚════╝ 
                                 """, 'red'))
print(colored(" [ 6v Spoofer | Github: @0xffvirus ]\n", 'red'))
print("""[1] Email Spoofer | [2] Fake Credit Card | 
[3] Fake Address | [4] Fake Ip \n""")

Options()
