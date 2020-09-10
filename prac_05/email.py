"""
CP1404/CP5632 Practical
Email to name dictionary
"""


def main():
    email_dict = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirm = input("Is your name {}? (Y/n) ".format(name))
        if confirm.upper() != "Y" and confirm != "":
            name = input("Name: ")
        email_dict[email] = name
        email = input("Email: ")
    for email, name in email_dict.items():
        print("{} ({})".format(name, email))


def get_name(email):
    parts = email.split("@")[0].split(".")
    name = " ".join(parts).title()
    return name


main()
