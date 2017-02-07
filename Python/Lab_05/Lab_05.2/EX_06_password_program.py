#Kristen Ching
def passCheck():
    global username
    global password
    username = input("Please enter your username. ")
    password = input("Please enter your password. ")
    if username == "ao":
        username = True
    else:
        username = False
    if password == "aery485":
        password = True
    else:
        password = False
    if password and username:
        print("You have been granted access.")
    elif password and not username:
        print("Username is invalid.")
        passCheck()
    elif username and not password:
        print("Password is invalid.")
        passCheck()
    elif not username and not password:
        print("Username and password are incorrect.")
        passCheck()
        
passCheck()
