from app import register, login

running = True

while running:
    print("**********Welcome to Bank Neodynamics.**********")
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
        login()
    elif selected_option == 3:
        print("Thanks for banking with us, do have a nice day.")
        running = False
