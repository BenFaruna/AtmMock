from datetime import datetime

from deposit_withdraw import check_balance, deposit, withdraw
from reg_login import register, login

running = True

while running:
    date = datetime.strftime(datetime.now(), format="%d/%m/%Y")
    time = datetime.strftime(datetime.now(), format="%H:%M")
    print("**********Welcome to Bank Neodynamics.**********")
    print(f"The time is {time}")
    print(f"Current date: {date}")
    print("""
Would you like to:
1. Register with us
2. Login
3. Come back another time
    """)

    selected_option = int(input("Please select an option: "))

    if selected_option == 1:
        register()
    elif selected_option == 2:
        user = login()
        
        while user:
            print("""
What operation would you like to carry out on your account:
1. Withdrawal
2. Deposit
3. Check balance
4. Logout
        """)
            bank_operations = int(input("Input: "))

            if bank_operations == 1:
                amount = int(input("Enter amount you want to withdraw: "))
                withdraw(user[0], amount)
            
            elif bank_operations == 2:
                amount = int(input("Enter amount you want to deposit: "))
                deposit(user[0], amount)
            
            elif bank_operations == 3:
                print(f"Your account balance is: ${check_balance(user[0])}")

            elif bank_operations == 4:
                print("Account logged out successfully.")
                print("Thank you for banking with us.\n")
                break
                


    elif selected_option == 3:
        print("Thanks for banking with us, do have a nice day.")
        running = False
