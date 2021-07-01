def print_reciept(L, total_cost):
    for i in range(0, len(L)):
        if L[i][2] > 0:
            output = "You have ordered {} {} pizza/s at ${} each".format(L[i][2], L[i][0],  L[i][1])
            amount = total_calculator(L, total_cost)
            output2 = "This total is ${} ". format(amount)
            print(output)
            print(output2)

def print_with_indexes(L):
    for i in range(0, len(L)):
        output = "{}: {}: {} : {}".format(i, L[i][0], L[i][1], L[i][2])
        print(output)

def total_calculator(L, total_cost):
    for i in range(0, len(L)):
        total_cost += L[i][2] * L[i][1]
        return total_cost


def add_pizza(L, total_cost):
    print_with_indexes(L)
    my_index = get_user_input(0, 2, "Please select what index number, would you like to add pizza to?   ")
    new_amount = get_user_input(1, 5, "How many of the pizza do you want to add?     ")
    L[my_index][2] += new_amount
    print_reciept(L, total_cost)


def subtract_pizza(L):
    print_with_indexes(L)
    my_index = get_user_input(0, 2, "Please select what index number, would you like to subtract pizza from?   ")
    new_amount = get_user_input(1, 5, "How many of the pizza do you want to subtract?     ")
    L[my_index][2] -= new_amount
    print_with_indexes(L)

def delivery_option (total_cost):
    output = """
    1: Delivery, this comes with an extra cost of $3 
    2: Pick up, you come in store to pick up at no extra cost 
    
    """
    print(output)
    choice = get_user_input(1, 2, "Which option would you like?  ")
    if choice == 1:
        total_cost += 3
        address = check_varible(6, 50, "Where would you like your pizza/s delivered to?     " )
        name = check_varible(2, 25, "Please enter your name:     ")
        number = check_phone_number(8, 12, "What is your phone number?   ")
        print("Your pizza/s will be delivered to {}" .format(address))
        print("Your pizza/s are now under the name {}".format(name))
        print("The phone number the pizza/s is associated with will be {}".format(number))
        customer_details = [name, number, address]
        return customer_details
    elif choice == 2:
        print("You have chosen pickup ")
        name = check_varible(2, 25, "Please enter your name:     ")
        number = check_phone_number (8, 12, "What is your phone number?   ")
        print("Your pizza/s are now under the name {}" .format(name))
        print("The phone number the pizza/s is associated with will be {}".format(number))
        customer_details = [name, number]
        return customer_details


def get_user_input (lower, higher, output):
    getting_input = True
    while getting_input == True:
        try:
            user_input = int(input(output))
        except ValueError:
            print("You have not entered an integer")
            continue
        if user_input < lower or user_input > higher:
            print("you have not entered a number between {} and {}".format(lower, higher))
            continue
        getting_input = False

    return user_input

def check_phone_number(lower, higher, output):
    getting_input = True
    while getting_input == True:
        try:
            user_input = int(input(output))
        except ValueError:
            print("You have not entered an integer")
            continue
        if user_input:
            continue
        getting_input = False


def check_varible (min, max, output):
    get_name = True
    while get_name == True:
        name = input(output)
        name = name.title()
        if len(name) > max:
            print('Sorry you have entered something with too many characters')
            continue
        elif len(name) < min:
            print("Sorry you have enter something with to little characters")
            continue

        get_name = False

    return name


def main_loop():
    run = True
    total_cost = 0
    my_L = [
        ["Margarita", 18.5, 0],
        ["Piccolo", 18.5, 0],
        ["La Prima Donna", 25.5, 0],
    ]
    while run == True:
        my_menu = """
        Press 
        'q' to quit
        'r' to review the see the menu
        'a' to add pizzas to the order
        'c' to choice how you want to receive the pizza/s
        's' to subtract a pizza/s
        'd' to delete the whole order

        """
        print(my_menu),
        user_choice = input("please enter your option here:    ")
        if user_choice == "q":
            print("Loop has stopped, Thank you")
            run = False
        elif user_choice == "r":
            print_with_indexes(my_L)
        elif user_choice == "a":
            add_pizza(my_L, total_cost)
        elif user_choice == "c":
            delivery_option(total_cost)
        elif user_choice == "s":
            subtract_pizza(my_L)
        elif user_choice == "d":
            run == False
        else:
            print("sorry your answer was not valid")


main_loop()

