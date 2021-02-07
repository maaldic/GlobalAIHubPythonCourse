userName = input("Please enter your username: ")
password = input("Please enter your password: ")
dict = {userName:"maaldic" , password:"1234"}

if dict[userName] == userName and dict[password]==password:
    print ("Welcome", userName)
else:
    print("Invalid access!")
