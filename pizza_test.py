

def print_with_indexes(L):
    for i in range(0, len(L)):
        output = "{}: {}: {} : {}".format(i, L[i][0], L[i][1], L[i][2])
        print(output)


def add_pizza(L):
    print_with_indexes(L)
    my_index = get_user_input(0, 2, "Please select what index number, would you like to add pizza to?   ")
    new_amount = get_user_input(1, 5, "How many of the pizza do you want to add?     ")
    L[my_index][2] += new_amount
    print_with_indexes(L)

def delivery_option (total_cost):
    output = """
    1: Delivery, this comes with an extra cost of $3 
    2: Pick up, you come in store to pick up at no extra cost 
    
    """
    print (output)
    choice = get_user_input(1,2, "Which option would you like?  ")
    if choice == 1:
        total_cost += 3
        address = input("Where would you like your pizza/s delivered too:    ")
        print("Your pizza/s will be delivered to {}" .format(address))
        return address
    elif choice == 2:
        print("You have chosen pickup ")
        name = check_name()
        print("Your pizza/s are now under the name {}" .format(name))



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


def check_name ():
    get_name = True
    while get_name == True:
        name = input("Please enter your name:     ")
        name = name.title()
        if len(name) > 25:
            print('Sorry you have entered something with too many chracters')
            continue
        elif len(name) < 2:
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

        """
        print(my_menu),
        user_choice = input("please enter your option here:    ")
        if user_choice == "q":
            print("Loop has stopped, Thank you")
            run = False
        elif user_choice == "r":
            print_with_indexes(my_L)
        elif user_choice == "a":
            add_pizza(my_L)
        elif user_choice == "c":
            delivery_option(total_cost)
        else:
            print("sorry your answer was not valid")


main_loop()
