def FakeIp():
    from faker import Faker
    from termcolor import colored
    fake = Faker()
    print("[ This Tool Generates random ipv4 & ipv6 not changing it ! ]")
    print("====== Fake Ip Address ======")
    print(colored("ipv4:", 'red'),fake.ipv4()) # Generates Fake ipv4
    print(colored("ipv6:", 'red'),fake.ipv6()) # Generates Fake ipv6
    input(colored("Press Enter to exit ...", 'red'))