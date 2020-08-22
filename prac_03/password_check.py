PASSWORD_MIN = 5
password = input("Password: ")
while len(password) < PASSWORD_MIN:
    print("Password must be minimum {} characters".format(PASSWORD_MIN))
    password = input("Password: ")
print(len(password) * "*")
