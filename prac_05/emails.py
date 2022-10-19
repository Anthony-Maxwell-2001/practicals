"""
Emails
Estimated: 25 minutes
Actual:
"""


def main():
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        email = input("Email: ")


def extract_name_from_email(email):
    first_half = email.split('@')[0]
    names = first_half.split('.')
    name = " ".join(names).title()
    return name


main()
