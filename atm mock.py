allowed_users = ["Seyi", "Mike", "Love"]
allowed_password = ["passwordSeyi", "passwordMike", "passwordLove"]

name = input("What is your name? \n")

if (name in allowed_users):
    password = input("Your password? \n")
    user_id = allowed_users.index(name)

    if (password == allowed_password[user_id]):

        print("Welcome %s" % name)
        print("These are the availale options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")

        selected_option = int(input("Plese select an option: "))

        if (selected_option == 1):
            print("You selected %s" % selected_option)

        elif (selected_option == 2):
            print("You selected %s" % selected_option)

        elif (selected_option == 3):
            print("You selected %s" % selected_option)

        else:
            print("Invalid Option selected, please try again")

    else:
        print("Password Incorrect, please try again")

else:
    print("Name not found, please try again")
