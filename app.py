import json, random

from getpass import getpass

def register():
    password = ''
    pass_confirm = None
    first_name = input("Enter first name: ")
    last_name = input("Enter Surname: ")
    email = ("Enter email address: ")
    account_number = random.randint(1111111111, 9999999999)
    print("Password is used to access account. Keep safe!!!")
    while password != pass_confirm:
        password = getpass("Enter password: ")
        pass_confirm = getpass("Confirm password: ")

        if password != pass_confirm:
            print("Password do not match. Enter correct passwod")

        else:
            user_details = {
                "first name": first_name,
                "last name": last_name,
                "email": email,
                "balance": 0,
                "password": password
            }
            with open(f"data/{account_number}.json", "w") as f:
                json.dump(user_details, f)
            print("Account created successfully.")
            print("Log in using account number to view balance.")

register()
