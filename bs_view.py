def show_menu():
    print()
    print("Welcome to Battleships !")
    print()
    print("[1] Play")
    print()
    print("[2] Exit")
    print()

def show_sub_menu():
    print()
    print("Ready to enter row & column co-ordinates, the board is 5x5 ?")
    print()
    print("[1] Enter co-ordinates")
    print()
    print("[2] Exit")
    print()

def get_input():
    print()
    print("Your choice: ", end="")
    return input()

def get_attack_details(param):
    print()
    print("Your ", param, " choice, pls enter 1-5: ", end="")
    return input()

def get_congrats_msg():
    print()
    print("Congratulations, you've sunk my Battleship !")
    print()

def get_board_details(attack_response):
    print()
    for row in attack_response:
        print((" ".join(row)))
    print()
    print("Jolly bad luck old chap, have another pop !")
    print()
    
    
