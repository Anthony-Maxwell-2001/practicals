"""CP1404 Password Stars"""


def main():
    minium_password_length = 8
    password_name = get_password(minium_password_length)
    print_asterisks(password_name)


def print_asterisks(password_name):
    print(len(password_name) * '*')


def get_password(minium_password_length):
    password_name = input("Enter Password: ")
    while len(password_name) < minium_password_length:
        print("Invalid password length")
        password_name = input("Enter Password: ")
    return password_name


main()
