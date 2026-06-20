username= input("enter the username:")
if username == "admin":
    password = input("enter the password:")

    if password == "1234":
        print("login is successful")
    else:
        print("wrong password")
else:
    print("Invalid username")