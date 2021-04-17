import json

def deposit(acct_no, amount):
    with open(f"data/{acct_no}.json", "r") as f:
        acct_details = json.load(f)
        acct_details['balance'] =  acct_details['balance'] + amount
    
    with open(f"data/{acct_no}.json", "w") as f:
        json.dump(acct_details, f, indent=4)


def withdraw(acct_no, amount):
    with open(f"data/{acct_no}.json", "r") as f:
        acct_details = json.load(f)
        if acct_details['balance'] < amount:
            print("Insufficient Balance.")
        else:
            acct_details['balance'] =  acct_details['balance'] - amount
    
    with open(f"data/{acct_no}.json", "w") as f:
        json.dump(acct_details, f, indent=4)

def check_balance(acct_no):
    with open(f"data/{acct_no}.json", "r") as f:
        acct_details = json.load(f)
    
    return acct_details['balance']
