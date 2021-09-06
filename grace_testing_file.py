import re

def get_user_input(lower, higher, output):
    """Check if number is between lower and higher.

    :param lower: integer
    :param higher: integer
    :param output: integer
    :return: integer
    """
    getting_input = True
    while getting_input is True:
        try:
            user_input = int(input(output))
        except ValueError:
            print("You have not entered an integer")
            continue
        if user_input < lower or user_input > higher:
            print("you have not entered a number "
                  "between {} and {}".format(lower, higher))
            continue
        return user_input

def get_single_input(output):
        """Validation for user input using an output.

        :param output: string
        :return: string
        """
        get_input = True
        while get_input is True:
            user_input = input(output)

            if user_input not in ['yes', 'no']:
                print("You have not entered yes or no try again")
                continue
            return user_input

def check_phone_number(output):
    """Search through list.

    :param output: string
    :return: integer
    """
    getting_input = True
    while getting_input is True:
        user_input = (input(output))
        x = re.search(
            "(^\\([0][3]\\))(\\d{7}$)|(^\\([0][4]\\))(\\d{7}$)|"
            "(^\\([0][6]\\))(\\d{7}$)|(^\\([0][7]\\))(\\d{7}$)|"
            "(^\\([0][9]\\))(\\d{7}$)|(^\\([0][2][1]\\))(\\d{6,8}$)|"
            "(^\\([0][2][2]\\))(\\d{6,8}$)|(^\\([0][2][7]\\))(\\d{6,8}$)|"
            "(^\\([0][2][9]\\))(\\d{6,8}$)|([0][8][0][0])([\\s])(\\d{5,8}$)",
            user_input)
        if x:
            return user_input
        else:
            print("Sorry your phone number was not at match")
            continue
def check_variable(min_, max_, output):
    """Check that string is between max and min.

    :param min_: integer
    :param max_: integer
    :param output: string
    :return: string
    """
    get_name = True
    while get_name is True:
        name = input(output)
        name = name.title()
        # if the word is greater than max
        if len(name) > max_:
            print('Sorry you have entered something with too many characters')
            continue
        # if the word is less than min
        elif len(name) < min_:
            print("Sorry you have enter something with to little characters")
            continue
        else:
            return name


if __name__=="__main__":
    print("testing integer input")
    output= get_user_input(0,5, "Please enter the number of pizzas:  ")
    print(output)
    print()
    print("Testing yes no confirm")
    output= get_single_input("Please confirm (yes/no):  ")
    print(output)
    print()
    print("Testing phone number")
    output= check_phone_number("Please enter phone number:  ")
    print(output)
    print("Testing name")
    output = check_variable(2,25,"Please enter your name:  ")
    print(output)
        
