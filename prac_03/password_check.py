PASSWORD_MIN = 5


def main():
    password = get_password(PASSWORD_MIN)
    print_password(password)


def print_password(password):
    print(len(password) * "*")


def get_password(PASSWORD_MIN):
    password = input("Password: ")
    while len(password) < PASSWORD_MIN:
        print("Password must be minimum {} characters".format(PASSWORD_MIN))
        password = input("Password: ")
    return password


main()
