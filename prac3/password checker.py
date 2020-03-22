'''
CP1404 Practical
password checker
'''

minimum_length = 8


def main():
    get_password()


def get_password():
    password = input("Enter password of at least {} characters:".format(minimum_length))
    if len(password) < minimum_length:
        print("*" * len(password))

main()
