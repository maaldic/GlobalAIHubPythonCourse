userName = "maaldic"
password = "1234"

x = input("Please enter your username: ")
y = input("Please enter your password: ")

if x==userName and y==password:
    print("Access successful!")
elif x==userName and y!=password:
    print("Password is wrong!")
elif x!=userName and y==password:
    print("Username is wrong!")
else:
    print("Username and the password are wrong!")
