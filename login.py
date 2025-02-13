# This program will break if the user entered their password wrong 3 times

#Set user name and password
print("Let us register your user name and password")
user = input("Create your user name: ")
password = input("Create your password: ")
print("\n" * 1000)

print("Thanks for registering. OK so lets log in.\n")

n=3

while n!=0:
    n=n-1
    if n ==3:
        break
    inuser = input("What is the your user name?: ")
    inpassword = input("What is your password?: ")
    if inuser == user and inpassword == password:
        print("That is the correct Credential. You now have access to your account")
        print(f"Welcome to your account {user}")
        n=4
    elif n>0:
        print(f"Wrong credentials, you have {n} more attempts ")
    if n == 0: 
        print("You have no more attempts. You are now locked out of your account. Please contact your admin")
