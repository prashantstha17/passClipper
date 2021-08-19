import csv, sys, pyperclip

path = input("Enter the path of your password csv file: ")
users = {}
with open(path) as file:
    read = csv.DictReader(file)
    for row in read:
        users[row['name']] = row


if len(sys.argv) < 2:
    print("Usage python PassClipper.py [website]")
    exit()
account = sys.argv[1]

if account in users:
    pyperclip.copy(users[account]['password'])
    print(f"Password for {account} is copied to clipboard")
else:
    print(f'No password saved for this {account}')
