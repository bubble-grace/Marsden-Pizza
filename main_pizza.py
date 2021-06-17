def print_with_indexes(L):
    for i in range(0, len(L)):
        output = "{}: {}: {}".format( i,L[i][0],L[i][1])
        print( output )

run = True
def main_loop():
    run = True
    my_L = [
        ["Margarita", 18.5],
        ["Piccolo", 18.5],
        ["La Prima Donna", 22.5],
    ]
    while run == True:
        user_choice = input ("""
        Press 
        'q' to quit
        'r' to review the see the menu
        
        please enter your option here:     
        """)
        if user_choice == "q":
            print("Loop has stopped, Thank you")
            run = False
        elif user_choice == "r":
            print_with_indexes(my_L)
        else:
            print ("sorry your answer was not valid")

main_loop()