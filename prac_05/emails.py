"""
Emails
Estimated: 25 minutes
Actual:
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n): ").upper()
        if confirmation != 'Y' and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    display_names_and_emails(email_to_name)


def extract_name_from_email(email):
    first_half = email.split('@')[0]
    names = first_half.split('.')
    name = " ".join(names).title()
    return name


def display_names_and_emails(email_to_name):
    for name, email in email_to_name.items():
        print(f"{name} ({email})")


main()
