import re


def checking_everthing(D, C, T, run):
    print_delivery(D)
    if T == 3:
        print("Sorry you have not ordered any pizzas")
        run = True
        return(run)
    elif T == 0:
        print("Sorry you have not ordered any pizzas")
        run = True
        return (run)
    else:
        print_reciept(C, T)

    yn = get_single_input()
    if yn == "yes":
        print("Thank you all your details are sorted")
    else:
        run = True
        return (run)

def update_delivery(D):
    print_delivery(D)
    my_index = get_user_input(0, 2, "Chose index number your would like to change ? ")
    if my_index == 0:
        new_address = check_varible(6, 50, "Where would you like your pizza/s delivered to?     ")
        old_address = D[my_index][1]
        D[my_index][1] = new_address
        print("The name {} has been changed to {}".format(old_address, new_address))
        print_with_indexes(D)
    elif my_index == 1:
        new_name = check_varible(2, 25, "Please enter your name:     ")
        old_name = D[my_index][1]
        D[my_index][1] = new_name
        print("The name {} has been changed to {}".format(old_name, new_name))
        print_delivery(D)
    elif my_index == 2:
        new_number = check_phone_number("What is your phone number? Please format (021)035689 with the prefix or area code in the ()  ")
        old_number = D[my_index][1]
        D[my_index][1] = new_number
        print("The name {} has been changed to {}".format(old_number, new_number))
        print_delivery(D)

    else:
        print("Sorry you have not entered 0, 1 or 2")






def delivery_option(D, total_amount):
    output = """
    1: Delivery, this comes with an extra cost of $3 
    2: Pick up, you come in store to pick up at no extra cost 

    """
    print(output)
    choice = get_user_input(1, 2, "Which option would you like?  ")
    if choice == 1:
        address = check_varible(6, 50, "Where would you like your pizza/s delivered to?     ")
        name = check_varible(2, 25, "Please enter your name:     ")
        number = check_phone_number( "What is your phone number? Please format (021)035689 with the prefix or area code in the ()  ")
        print("Your pizza/s will be delivered to {}".format(address))
        print("Your pizza/s are now under the name {}".format(name))
        print("The phone number the pizza/s is associated with will be {}".format(number))
        D.append(["address", address])
        D.append(["name", name])
        D.append(["phone number", number])
        print("----" * 10)
        total_amount += 3
        return total_amount
    elif choice == 2:
        print("You have chosen pickup ")
        name = check_varible(2, 25, "Please enter your name:     ")
        number = check_phone_number( "What is your phone number? Please format (021)035689 with the prefix or area code in the ()  ")
        print("Your pizza/s are now under the name {}".format(name))
        print("The phone number the pizza/s is associated with will be {}".format(number))
        D.append(["name", name])
        D.append(["phone number", number])
        print("----" * 10)
    return D

def check_phone_number(output):
    getting_input = True
    while getting_input == True:
        user_input = (input(output))
        x = re.search("(^\([0][3]\))(\d{7}$)|(^\([0][4]\))(\d{7}$)|(^\([0][6]\))(\d{7}$)|(^\([0][7]\))(\d{7}$)|(^\([0][9]\))(\d{7}$)|"
                      "(^\([0][2][1]\))(\d{6,8}$)|(^\([0][2][2]\))(\d{6,8}$)|(^\([0][2][7]\))(\d{6,8}$)|(^\([0][2][9]\))(\d{6,8}$)|"
                      "([0][8][0][0])([\s])(\d{5,8}$)", user_input)
        if x:
            getting_input = False
        else:
            print("Sorry your phone number was not at match")
            continue
        return user_input



def get_single_input():
   get_input = True
   while get_input == True:
       user_input = input("Please enter yes if the details are correct and no if they are not   ---->")
       print (user_input)

       if user_input not in ['yes', 'no']:
           print ("You have not entered yes or no try again")
           continue

       get_input = False
       return user_input

def print_delivery(D):
    print("----" * 10)
    for i in range(0, len(D)):
        output = "{:3} : {:10} : {:10}".format(i, D[i][0], D[i][1])
        print(output)
    print("----" * 10)

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

def print_reciept(C, total_amount):
    print("----" * 10)
    for i in range(0, len(C)):
        if C[i][2] > 0:
            output = "You have ordered {} {} pizza/s at ${} each".format(C[i][2], C[i][0],  C[i][1])
            print(output)
    total_amount += total_calculator(C)
    output2 = "This total is ${} ". format(total_amount)
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


def add_pizza(L, C, max_per_pizza, total_amount):
    print_with_indexes(L)
    my_index = get_user_input(0, len(L)-1, "Please select what index number, would you like to add pizza to?   ")
    new_amount = get_user_input(1, max_per_pizza, "How many of the {}/s do you want to add?     " .format(L[my_index][0]))
    temp = [L[my_index][0], L[my_index][1], new_amount]
    C.append(temp)
    print_reciept(C, total_amount)



def subtract_pizza(C, total_amount):
    print_with_indexes_2(C)
    my_index = get_user_input(0, len(C)-1, "Please select what index number, would you like to subtract pizza from?   ")
    sub_amount = get_user_input(0, C[my_index][2], "How many of the pizza do you want to subtract?     ")
    new_amount = C[my_index][2] - sub_amount
    C[my_index][2] = new_amount
    print_reciept(C, total_amount)

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
        ["u", "to update the customer details"],
        ["c", "to confirm the details of the order"],
    ]
    customer_list =[]
    customer_details =[]
    total_amount = 0
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
            add_pizza(pizza_list, customer_list, max_per_pizza, total_amount)
        elif user_choice == "s":
            subtract_pizza(customer_list, total_amount)
        elif user_choice == "r":
            print_reciept(customer_list, total_amount)
        elif user_choice == "d":
            total_amount = delivery_option(customer_details, total_amount)
        elif user_choice == "u":
            update_delivery(customer_details)
        elif user_choice == "c":
            run = checking_everthing(customer_details,customer_list, total_amount, run)
        else:
            print("sorry your answer was not valid")
            print("----" * 10)


main_loop()