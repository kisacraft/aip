print("Enter your name:")

name = input()

if name == ("admin" or "Admin"):
    print("full")
elif name == ("User" or "user"):
    print("Hello, User!")
else:
    print("Access denied!")