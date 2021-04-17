import json, random

from getpass import getpass
from os import path

def gen_account_number():
    return random.randint(1111111111, 9999999999)

def register():
    password = ''
    pass_confirm = None
    account_exists = False

    first_name = input("Enter first name: ")
    last_name = input("Enter Surname: ")
    email = input("Enter email address: ")
    account_number = gen_account_number()

    while not account_exists:

        if path.exists(f"data/{account_number}.json"):
            account_number = gen_account_number()
            print(path.exists(f"data/{account_number}.json"))
            continue
        else:
            account_exists = True
            

    print("Password is used to access account. Keep safe!!!")
    while password != pass_confirm:
        password = getpass("Enter password: ")
        pass_confirm = getpass("Confirm password: ")

        if password != pass_confirm:
            print("Password do not match. Enter correct password")

        else:
            user_details = {
                "first name": first_name,
                "last name": last_name,
                "email": email,
                "password": password,
                "balance": 0
            }
            with open(f"data/{account_number}.json", "w") as f:
                json.dump(user_details, f, indent=4)
            print("Account created successfully.")
            print(f"Account number: {account_number}")
            print("Log in using account number to perform operations on your account.")

def login():
    account_number = input("Enter your account number: ")
    password = getpass("Enter your password: ")
    logged_in = False

    if path.exists(f"data/{account_number}.json"):
        with open(f"data/{account_number}.json") as f:
            account_details = json.load(f)

            while not logged_in:
                if password == account_details["password"]:
                    logged_in = True
                    print("Account logged in successfully.")
                    print(f"Welcome {account_details['first name']} {account_details['last name']}")
                else:
                    print("Incorrect password. Try again.")
                    password = getpass("Enter password: ")

    else:
        print("Invalid account number.")
        print("Please check the account number and try again.")
