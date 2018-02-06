def login():
    username = input("Input Username: ")
    if username.upper() != "ROHAN":
        print("--ACCESS DENIED--")
    else:
        password = input("Input Password: ")
        if password.upper() != "JACK IS A LOSER":
            print("INCORRECT")
        else:
            print("Welcome")

if __name__ == "__main__":
    login()