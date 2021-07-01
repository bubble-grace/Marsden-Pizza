def print_reciept(L, total_cost):
    print("----" * 10)
    for i in range(0, len(L)):
        if L[i][2] > 0:
            output = "You have ordered {} {} pizza/s at ${} each".format(L[i][2], L[i][0],  L[i][1])
            print(output)
    amount = total_calculator(L, total_cost)
    output2 = "This total is ${} ". format(amount)
    print(output2)
    print("----" * 10)

def print_with_indexes(L):
    for i in range(0, len(L)):
        output = "{}: {}: {} : {}".format(i, L[i][0], L[i][1], L[i][2])
        print(output)

def total_calculator(L, total_cost):
    total = 0
    for i in range(0, len(L)):
        sub = L[i][2] * L[i][1]
        total += sub
    return total


def add_pizza(L, total_cost):
    print_with_indexes(L)
    my_index = get_user_input(0, 2, "Please select what index number, would you like to add pizza to?   ")
    new_amount = get_user_input(1, 5, "How many of the pizza do you want to add?     ")
    L[my_index][2] += new_amount
    print_reciept(L, total_cost)


def subtract_pizza(L, total_cost):
    print_with_indexes(L)
    my_index = get_user_input(0, 2, "Please select what index number, would you like to subtract pizza from?   ")
    new_amount = get_user_input(1, 5, "How many of the pizza do you want to subtract?     ")
    L[my_index][2] -= new_amount
    print_reciept(L, total_cost)

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
        's' to subtract a pizza/s

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
        elif user_choice == "s":
            subtract_pizza(my_L, total_cost)
        else:
            print("sorry your answer was not valid")


main_loop()