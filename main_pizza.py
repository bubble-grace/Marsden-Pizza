"""A pizza order program to store information."""

import re


# get all lists
# ask for input


def checking_everything(d, c, total_amount):
    """Invoicing the customer with details.

    :param d: list
    :param c: list
    :param total_amount:
    :return: boolean, integer
    """

    if len(c) == 0:
        print("Sorry you have not ordered any pizzas")
        run = True
        return run, total_amount
    elif len(d) == 0:
        print("You have not entered details "
              "for pick up/delivery")
        run = True
        return run, total_amount
    else:
        # print details
        print_delivery(d)
        print("----" * 10)
        print_receipt(c, total_amount)
        print("----" * 10)
        # confirm with user
        output = "Please enter yes if the details" \
                 " are correct and no if they are not---->"
        yn = get_single_input(output)
        if yn == "yes":
            print("Thank you all your details are sorted")
            get = get_single_input("Would you like to start another order?")
            if get == "yes":
                c.clear()
                d.clear()
                total_amount = 0
                run = True
                return run, total_amount
            else:
                run = False
                return run, total_amount
        else:
            run = True
            return run, total_amount

# need to get input from user
# change customer list


def update_delivery(d):
    """Change delivery information.

    :param d: list
    :return: boolean
    """
    # if nothing in list
    if len(d) == 0:
        print("You have not entered details for pick up/delivery")
        run = True
        return run
    else:
        print_delivery(d)
        output = "Chose index number your would like to change ? "
        # get index
        my_index = get_user_input(0, 2, output)
        # name variable
        if my_index == 0:
            new_name = check_variable(2, 25, "Please enter your name:     ")
            old_name = d[my_index][1]
            d[my_index][1] = new_name
            print("The name {} has been changed to {}".format(old_name, new_name))
            print_delivery(d)
            run = True
            return run
        # phone number variable
        elif my_index == 1:
            output = "What is your phone number? Please format " \
                     "(021)035689 with the prefix or area code in the ()"
            new_number = check_phone_number(output)
            old_number = d[my_index][1]
            d[my_index][1] = new_number
            print("The name {} has been changed to {}"
                  .format(old_number, new_number))
            print_delivery(d)
            run = True
            return run
        # address variable
        elif my_index == 2:
            output2 = "Where would you like your pizza/s delivered to?     "
            new_address = check_variable(6, 50, output2)
            old_address = d[my_index][1]
            d[my_index][1] = new_address
            print("The name {} has been changed to {}"
                  .format(old_address, new_address))
            print_with_indexes(d)
            run = True
            return run
        else:
            # basic validation
            print("Sorry you have not entered 0, 1 or 2")
            run = True
            return run


# get user input
# format user input


def delivery_option(d, total_amount):
    """Asking the user for details surrounding delivery.

    :param d: list
    :param total_amount: integer
    :return: None
    """
    if len(d) > 1:
        print("You have already entered details for pick up/delivery")
        return total_amount, d
    else:
        output = """
        1: Delivery, this comes with an extra cost of $3
        2: Pick up, you come in store to pick up at no extra cost
    
        """
        print(output)
        # get 1 or 2
        choice = get_user_input(1, 2, "Which option would you like?  ")
        if choice == 1:
            output = "Where would you like your pizza/s delivered to?     "
            # get address
            address = check_variable(6, 50, output)
            # get name
            name = check_variable(2, 25, "Please enter your name:     ")
            # get phone number
            output = "What is your phone number? Please format (021)035689 " \
                     "with the prefix or area code in the ()  "
            number = check_phone_number(output)
            # confirmation print out
            print("Your pizza/s will be delivered to {}".format(address))
            print("Your pizza/s are now under the name {}".format(name))
            print("The phone number the pizza/s is "
                  "associated with will be {}".format(number))
            # add to list
            d.append(["name", name])
            d.append(["phone number", number])
            d.append(["address", address])
            print("----" * 10)
            total_amount += 3
            return total_amount, d
        elif choice == 2:
            print("You have chosen pickup ")
            # get name
            name = check_variable(2, 25, "Please enter your name:     ")
            # get phone number
            output = "Please format (021)035689 with " \
                     "the prefix or area code in the ()  "
            print(output)
            number = check_phone_number("What is your phone number?")
            # confirmation
            print("Your pizza/s are now "
                  "under the name {}".format(name))
            print("The phone number the pizza/s is "
                  "associated with will be {}".format(number))
            # add to list
            d.append(["name", name])
            d.append(["phone number", number])
            print("----" * 10)
        return total_amount, d


# phone number validation
# search dictionary for possible options


def check_phone_number(output):
    """Search through list.

    :param output: string
    :return: integer
    """
    getting_input = True
    while getting_input is True:
        user_input = (input(output))
        # limitation for phone number
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
            # validation
            print("Sorry your phone number was not at match")
            continue


# validating yes or no
# get user input


def get_single_input(output):
    """Validation for user input using an output.

    :param output: string
    :return: string
    """
    get_input = True
    while get_input is True:
        user_input = input(output)
        # if it is not yes or no
        if user_input not in ['yes', 'no']:
            print("You have not entered yes or no try again")
            # the loop keeps going
            continue
        return user_input


# print delivery list


def print_delivery(d):
    """Print the list.

    :param d: list
    :return: None
    """
    print("----" * 10)
    # only for length of d to get index
    for i in range(0, len(d)):
        # format correctly
        output = "{:3} : {:10} : {:10}".format(i, d[i][0], d[i][1])
        print(output)
    print("----" * 10)


# check variable
# used for name and address


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


# prints nicely

def print_receipt(c, total_amount):
    """Print out customer invoice.

    :param c: list
    :param total_amount: integer
    :return: None
    """
    print("----" * 10)
    for i in range(0, len(c)):
        # if it has pizza/s
        if c[i][2] > 0:
            output = ("You have ordered {} {} pizza/s at ${:.2f} each"
                      .format(c[i][2], c[i][0], c[i][1]))
            print(output)
    # send to calculator function to get the total
    total_amount += total_calculator(c)
    output2 = "This total is ${:.2f} ".format(total_amount)
    print(output2)
    print("----" * 10)
    return None


# print 3 option list


def print_with_indexes(d):
    """Print the contents of a list with index numbers.

    :param d: list
    :return: None
    """
    # only for length of list get indices
    for i in range(0, len(d)):
        # print for multidimensional list (3)
        output = "{:3}: {:15}: {:6} ".format(i, d[i][0], d[i][1])
        print(output)
    return None


# print 4 option list


def print_with_indexes_2(d):
    """Print the contents of a list with index number.

    :param d: list
    :return: None
    """
    # only for length of list get indices
    for i in range(0, len(d)):
        # print for multidimensional list (4)
        output = "{:3}: {:15}: {:6} : {:3} ".format(
            i, d[i][0], d[i][1], d[i][2])
        print(output)
    return None

# gets lists
# multiplication for price


def total_calculator(c):
    """Working out the price to charge the customer.

    :param c: list
    :return: integer
    """
    # start at zero
    total = 0
    for i in range(0, len(c)):
        # the number of pizzas multiplied by the price
        sub = c[i][2] * c[i][1]
        total += sub
    return total


# look through a list
# search function


def search_for_name(c, pizza_name):
    """Looking through a list for a name.

    :param c: List
    :param pizza_name: float
    :return: integer
    """
    for i in range(0, len(c)):
        # if the name is the same as pizza name
        if c[i][0] == pizza_name:
            # return the index number of the pizza
            return i
    # return nothing
    return -1

# needs pizza order list
# needs name of pizza
# need to loop through the order list and check if any = name
# return the index number
# if nothing found
# return -1


def add_pizza(d, c, max_per_pizza, total_amount):
    """Adding values/updating customer order list.

    :param d: list
    :param c: list
    :param max_per_pizza: integer
    :param total_amount: float
    :return: None
    """
    cont = True
    while cont is True:
        # Add a pizza to the customer order
        print_with_indexes(d)
        message = "Please choose the index number of the pizza: "
        choice = get_user_input(0, (len(d) - 1), message)
        pizza_name = d[choice][0]
        result = search_for_name(c, pizza_name)
        if result == -1:
            # if the pizza has not all ready been ordered
            output = "How many of the {}/s do you want to add?     "
            new_amount = get_user_input(
                1, max_per_pizza, output.format(d[choice][0]))
            temp = [d[choice][0], d[choice][1], new_amount]
            c.append(temp)
            # print a nice output
            print_receipt(c, total_amount)
            return total_amount
        else:
            # tell if they have al ready ordered
            message = "You already have {} of the {} in the order"\
                .format(c[result][2], pizza_name)
            print(message)
            # new max amount to have a max total of 5 pizzas
            available_pizza = max_per_pizza - c[result][2]
            message = "You can order a maximum of {} more"\
                .format(available_pizza)
            print(message)
            # if they want more, how many?
            message = "How many more {} would you like?  "
            output = message.format(pizza_name)
            amount = get_user_input(0, available_pizza, output)
            c[result][2] += amount
            # print formated
            print_receipt(c, total_amount)
            return total_amount


# check if that pizza is already there
# if it is
# find out how many pizzas already have
# new max - max - the number already there
# communicate to user
# request amount
# then add to pre-existing amount


def subtract_pizza(c, total_amount):
    """Removing pizza/s from costumer list or subtracting pizza/s.

    :param c: list
    :param total_amount: integer
    :return: None
    """
    print_with_indexes_2(c)
    # get input for index number
    output = "Please select what index number, " \
             "would you like to subtract pizza from?   "
    my_index = get_user_input(0, len(c) - 1, output)
    output = "How many of the pizza do you want to subtract?     "
    # make sure the pizzas can not become negative
    sub_amount = get_user_input(0, c[my_index][2], output)
    new_amount = c[my_index][2] - sub_amount
    c[my_index][2] = new_amount
    # if this removes the type of pizzas altogether
    if new_amount == 0:
        c.pop(my_index)
    print_receipt(c, total_amount)
    return None


# takes two numbers and one string
# higher and lowers numbers are included in validation
# output is the message to the user


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
        # to allow the errors to give user second chance
        except ValueError:
            # targeted feedback
            print("You have not entered an integer")
            continue
        if user_input < lower or user_input > higher:
            # targeted feedback
            print("you have not entered a number "
                  "between {} and {}".format(lower, higher))
            continue
        # only if the input is correct return
        return user_input


# home of the code
# has lists


def main_loop():
    """Running all the functions.

    :return: None
    """
    run = True
    # starting max of pizza/s
    max_per_pizza = 5
    # what pizzas and price
    pizza_list = [
        ["Margarita", 18.5],
        ["Piccolo", 18.5],
        ["Calzone", 18.5],
        ["Numero Uno", 18.5],
        ["Peperoni", 18.5],
        ["Olivia", 18.5],
        ["Piccolo", 18.5],
        ["La Prima Donna", 25.5],
        ["Formaggio", 25.5],
        ["Madonna", 25.5]
    ]
    # the options for the phone operator
    my_menu = [
        ["q", "quit"],
        ["m", "the see the menu"],
        ["a", "to add pizzas to the order"],
        ["s", "to subtract a pizza/s"],
        ["r", "to see where the order is at"],
        ["d", "to chose the method of receiving your pizzas"],
        ["u", "to update the customer details"],
        ["c", "to confirm the details of the order"],
    ]
    customer_list = []
    customer_details = []
    total_amount = 0
    while run is True:
        for i in range(0, len(my_menu)):
            # print options for the phone operator
            output = "{} : {}".format(my_menu[i][0], my_menu[i][1])
            print(output)

        user_choice = input("please enter your option here: ->  ").lower()
        if user_choice == "q":
            # response to the phone operator wanting to leave
            print("Loop has stopped, Thank you")
            run = False
        elif user_choice == "m":
            # calling the function to print menu
            print_with_indexes(pizza_list)
        elif user_choice == "a":
            # calling function to add pizza/s
            add_pizza(pizza_list,
                      customer_list, max_per_pizza, total_amount)
        elif user_choice == "s":
            # calling function to subtract pizza/s
            subtract_pizza(customer_list, total_amount)
        elif user_choice == "r":
            # calling function to show all current details
            print_receipt(customer_list, total_amount)
        elif user_choice == "d":
            # calling function to sort out delivery
            total_amount, customer_details = delivery_option(
                customer_details, total_amount)
        elif user_choice == "u":
            # calling function to update delivery
            run = update_delivery(customer_details)
        elif user_choice == "c":
            # calling function to confirm order
            run, total_amount = checking_everything(customer_details, customer_list, total_amount)
        else:
            # basic validation
            print("sorry your answer was not valid")
            print("----" * 10)


# to call all functions and start the code
main_loop()
