from users import users
def login_user():
    print()
    user_name=input("Enter the user name:")
    password=input("Enter the password:")
    print("="*50)
    if user_name in users:
        if password == users[user_name]["password"]:
            print("="*50)
            print("LOGIN SUCCESSFUL")
            print("="*50)
            print("Welcome,",user_name,"!")
            print("="*50)
            return user_name,users[user_name]["email"]
    elif user_name not in users:
        print("="*50)
        print("❌ ERROR")
        print("\n Invlaid Username!")
        print("\n Please Try again.")
        print("="*50)
    elif user_name in users:
        if password!=users[user_name]["password"]:
            print("="*50)
            print("❌ ERROR")
            print("\n Invlaid Password!")
            print("\n Please Try again.")
            print("="*50)
    else:
        print("="*50)
        print("❌ ERROR")
        print("\n Invlaid  Username or Password!")
        print("\n Please Try again.")
        print("="*50)