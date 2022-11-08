def Fadd():
    from faker import Faker
    from termcolor import colored
    fake = Faker()
    def malegen():
        print(colored("Full Name:", "cyan"), f"{fake.prefix_male()} {fake.first_name_male()} {fake.last_name_male()}") # Fake Full Name
        print(colored("Address:", "cyan"), f"{fake.address()}") # Fake Address
        print(colored("Birthday:", "cyan"), f"{fake.date_of_birth(minimum_age=20, maximum_age=86)}") #Fake Birthdate with minimum and maximum age
        print("==================================")
    def femalegen():
        print(colored("Full Name:", "cyan"), f"{fake.prefix_female()} {fake.first_name_female()} {fake.last_name_female()}")
        print(colored("Address:", "cyan"), f"{fake.address()}")
        print(colored("Birthday:", "cyan"), f"{fake.date_of_birth(minimum_age=20, maximum_age=86)}")
        print("==================================")
    print("[1] Male | [2] Female")
    opt = int(input("Select Option: "))
    if opt == 1:
        print("==================================")
        for i in range(3):
            malegen()
        input(colored("Press Enter to exit ...", 'red'))
    elif opt == 2:
        print("==================================")
        for i in range(3):
            femalegen()
        input(colored("Press Enter to exit ...", 'red'))