
import bs_model
import bs_view

def run():
    mainmenu()

def mainmenu():
    while True:
        #Welcome menu
        bs_view.show_menu()
        selection = bs_view.get_input()        
        if selection == '1':
            #Create Gameboard object
            new_game = bs_model.Gameboard()
            #In-play menu
            bs_view.show_sub_menu()
            sub_selection = bs_view.get_input()   
            
            if sub_selection == '1':
                while True:
                    #Ask for row and col input
                    row = bs_view.get_attack_details("row")        
                    col = bs_view.get_attack_details("column")

                    #Call instance method 'attack', submitting row and col input,  
                    #if successfull then return true else return list for output
                    attack_response = new_game.attack(row, col)
                    if attack_response == True:
                        #Hit
                        bs_view.get_congrats_msg()
                        return
                    else:
                        #Miss: retry
                        bs_view.get_board_details(attack_response)        
            else:
                return
        else:
            return

if __name__ == "__main__":
    run()