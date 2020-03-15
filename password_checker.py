minimum = 5

def password_checker():
    """combine functions to get and check password"""
    password = get_password(minimum)
    print_asterisks(password)

def get_password(minimum):
    """ensure password is long enough"""
    password = input("Enter a minimum {} character password: ".format(minimum))
    while len(password) < minimum:
        print("Password is too short")
        password = input("Enter a minimum {} character password: ".format(minimum))
    return password

def print_asterisks(sequence):
    """return an asterisk for each character"""
    print('*' * len(sequence))

password_checker()