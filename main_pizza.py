import re

def delivery_option(D):
    output = """
    1: Delivery, this comes with an extra cost of $3 
    2: Pick up, you come in store to pick up at no extra cost 

    """
    print(output)
    choice = get_user_input(1, 2, "Which option would you like?  ")
    if choice == 1:
        address = check_varible(6, 50, "Where would you like your pizza/s delivered to?     ")
        name = check_varible(2, 25, "Please enter your name:     ")
        number = check_phone_number( "What is your phone number?   ")
        print("Your pizza/s will be delivered to {}".format(address))
        print("Your pizza/s are now under the name {}".format(name))
        print("The phone number the pizza/s is associated with will be {}".format(number))
        temp = [name, number, address]
        D.append (temp)
    elif choice == 2:
        print("You have chosen pickup ")
        name = check_varible(2, 25, "Please enter your name:     ")
        number = check_phone_number( "What is your phone number?   ")
        print("Your pizza/s are now under the name {}".format(name))
        print("The phone number the pizza/s is associated with will be {}".format(number))
        temp = [name, number]
        D.append(temp)

def check_phone_number(output):
    getting_input = True
    while getting_input == True:
        try:
            user_input = int(input(output))
        except ValueError:
            print("You have not entered an integer")
            continue
        getting_input = False
    return user_input

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

def print_reciept(C):
    print("----" * 10)
    for i in range(0, len(C)):
        if C[i][2] > 0:
            output = "You have ordered {} {} pizza/s at ${} each".format(C[i][2], C[i][0],  C[i][1])
            print(output)
    amount = total_calculator(C)
    output2 = "This total is ${} ". format(amount)
    print(output2)
    print("----" * 10)

def print_with_indexes(L):
    for i in range(0, len(L)):
        output = "{:3}: {:15}: {:6} ".format(i, L[i][0], L[i][1])
        print(output)

def print_with_indexes_2(L):
    for i in range(0, len(L)):
        output = "{:3}: {:15}: {:6} : {:3} ".format(i, L[i][0], L[i][1], L[i][2])
        print(output)

def total_calculator(C):
    total = 0
    for i in range(0, len(C)):
        sub = C[i][2] * C[i][1]
        total += sub
    return total


def add_pizza(L, C, max_per_pizza):
    print_with_indexes(L)
    my_index = get_user_input(0, len(L)-1, "Please select what index number, would you like to add pizza to?   ")
    new_amount = get_user_input(1, max_per_pizza, "How many of the {}/s do you want to add?     " .format(L[my_index][0]))
    temp = [L[my_index][0], L[my_index][1], new_amount]
    C.append(temp)
    print_reciept(C)



def subtract_pizza(C):
    print_with_indexes_2(C)
    my_index = get_user_input(0, len(C)-1, "Please select what index number, would you like to subtract pizza from?   ")
    sub_amount = get_user_input(0, C[my_index][2], "How many of the pizza do you want to subtract?     ")
    new_amount = C[my_index][2] - sub_amount
    C[my_index][2] = new_amount
    print_reciept(C)

# takes two numbers and one string
# higher and lowers numbers are included in validation
# output is the message to the user
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

def main_loop():
    run = True
    max_per_pizza = 5
    pizza_list = [
        ["Margarita", 18.5],
        ["Piccolo", 18.5],
        ["La Prima Donna", 25.5]
    ]
    my_menu = [
        ["q", "quit"],
        ["m", "the see the menu"],
        ["a", "to add pizzas to the order"],
        ["s", "to subtract a pizza/s"],
        ["r", "to see where the order is at"],
        ["d", "to chose the method of receiving your pizzas"],
    ]
    customer_list =[]
    customer_details =[]
    while run == True:
        for i in range(0, len(my_menu)):
            output = "{} : {}".format(my_menu[i][0], my_menu[i][1])
            print(output)


        user_choice = input("please enter your option here: ->  ")
        if user_choice == "q":
            print("Loop has stopped, Thank you")
            run = False
        elif user_choice == "m":
            print_with_indexes(pizza_list)
        elif user_choice == "a":
            add_pizza(pizza_list, customer_list, max_per_pizza)
        elif user_choice == "s":
            subtract_pizza(customer_list)
        elif user_choice == "r":
            print_reciept(customer_list)
        elif user_choice == "d":
            delivery_option(customer_details)
        else:
            print("sorry your answer was not valid")
            print("----" * 10)


main_loop()