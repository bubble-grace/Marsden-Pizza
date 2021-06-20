def print_with_indexes(L):
    for i in range(0, len(L)):
        output = "{}: {}: {} : {}".format( i,L[i][0],L[i][1], L[i][2])
        print( output )

def add_pizza(L):
    print_with_indexes(L)
    my_index = int(input("Please select what index number, would you like to add pizza to?   "))
    new_amount = int(input("How many of the pizza do you want to add?     "))
    if new_amount <= 5:
        L[my_index][2] += new_amount
        print_with_indexes(L)
    else:
        output = "Sorry your number is above 5, the max number of one type of pizza is 5"
        print (output)


run = True
def main_loop():
    run = True
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
     
        """
        print(my_menu),
        user_choice = input ("please enter your option here:    ")
        if user_choice == "q":
            print("Loop has stopped, Thank you")
            run = False
        elif user_choice == "r":
            print_with_indexes(my_L)
        elif user_choice == "a":
            add_pizza(my_L)
        else:
            print ("sorry your answer was not valid")

main_loop()