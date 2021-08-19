import csv, sys, pyperclip
if len(sys.argv) < 2:
    print("Usage python PassClipper.py [website]")
    sys.exit()
account = sys.argv[1]
print("""Choose your browser
1. Firefox
2. Chrome""")
browser = input()
path = input("Enter the path of your password csv file: ")
users = {}

if browser == "2":
    with open(path) as file:
        read = csv.DictReader(file)
        for row in read:
            users[row['name']] = row


elif browser == "1":
    with open(path) as file:
        read = csv.DictReader(file)
        for row in read:
            users[row['url']] = row



if account in users:
    pyperclip.copy(users[account]['password'])
    print(f"Password for {account} is copied to clipboard")
else:
    print(f'No password saved for this {account}')
