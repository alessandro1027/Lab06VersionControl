"""
Alessandro Giusti
COP3502C
Lab 6 Version Control
"""


def encode(password):
    dict_pw_keys = {'0': '3', '1': '4', '2': '5', '3': '6',
                    '4': '7', '5': '8', '6': '9', '7': '0',
                    '8': '1', '9': '2'}

    password_list = list(password)
    encoded_password = ''

    for i in range(len(password_list)):
        password_list[i] = dict_pw_keys.get(password_list[i])
        encoded_password += ''.join(password_list[i])

    return encoded_password
    # end encode(password) function


def decode(password):
    # collaborator will add this function
    pass


def display_menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")
    # display menu function


def main():

    # initialized vars
    decoded_password = ''
    encoded_password = ''

    # while loop for menu selection
    while True:
        display_menu()
        menu_selection = int(input("Please enter an option: "))

        # match statement to match the menu option selected
        match menu_selection:
            case 1:
                password = input("Please enter your password to encode: ")
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
                print(encoded_password)
            case 2:
                """
                decoded_password = decode(encoded_password)
                """
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            case 3:
                break
                # menu selection for user to quit
            case _:
                print("Invalid selection")
                # incase an int is inputted which is not in the menu


if __name__ == "__main__":
    main()
