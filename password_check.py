password=input("Enter your password:")
while len(password) < 10:
    print("Error!!!Pls enter again:")
    password = int(input("Enter your password:"))
else:
    print("*"*len(password))