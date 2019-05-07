import oo_bt_model
import bt_view


def run():
    #Call Class method to load all json file data 
    oo_bt_model.Account.load_datafile()
    mainmenu()

# TODO define separate login function
def login():
    pass

def mainmenu():
    while True:
        bt_view.show_menu()
        selection = bt_view.get_input()        
        #Account Creation
        if selection == '1':
            #account = None
            #pin = None
            #Gather account details
            f_name = bt_view.get_input_new_account("First Name")
            l_name = bt_view.get_input_new_account("Last Name")
            pin = bt_view.get_input_new_account("PIN")
            con_pin = bt_view.get_input_new_account("Confirm PIN")
            #Check if pins match
            if pin != con_pin:
                bt_view.get_pins_unmatched()
            else:
                #Create account, ie. add to data dictionary
                #OLD
                #account = oo_bt_model.create_account(f_name, l_name, pin)
                
                #NEW: Create account object, pass f_name, l_name, pin
                new_account = oo_bt_model.Account("", pin, "", f_name, l_name)
                #Call instance method 'create_account'
                bt_view.get_new_account_confirm(new_account.create_account())
        #Log In
        elif selection == '2':    
            #Gather account number and pin
            #account = None
            #pin = None
            new_balance = None
            account = bt_view.get_account_details("Account Number")
            pin = bt_view.get_account_details("PIN")
            #Return greeting

            # OLD if bt_model.validate_account(account, pin) == "xxx":
            #if not new_account.create_account():
            
            #NEW: Create account object, pass account & pin
            val_account = oo_bt_model.Account(account, pin, "", "", "")
            #Call instance method 'validate'
            if not val_account.validate():
                #Failed to find account
                bt_view.get_failed_validate_msg()
            else:
                #Welcome greeting
                #OLD
                #details = bt_model.load_account(account)
                # OLD CODE details = details + " (" + account + ")"
                #bt_view.get_login_greeting(details)

                #NEW: Create account object, pass account
                load_account = oo_bt_model.Account(account, "", "", "", "")
                #Call instance method 'validate'
                bt_view.get_login_greeting(load_account.load_account_data())
                
                while True:
                    #New sub-menu
                    bt_view.show_op2_menu()
                    op2_selection = bt_view.get_input() 
                    if op2_selection == '1':
                        #Check Bal
                        #OLD
                        #balance = bt_model.get_bal(account)
                        #bt_view.get_show_balance(balance)
                    
                        #NEW: Call instance method 'get_bal' to retrieve bal for load_account object
                        bt_view.get_show_balance(load_account.get_bal())
                    elif op2_selection == '2':
                        #Withdraw
                        amount = bt_view.get_with_or_dep_amount("Withdrawal Amount:")
                        #OLD
                        #new_balance = bt_model.withdraw(account, amount)
                        
                        #NEW: Call instance method 'withdraw' to deduct from bal for load_account object
                        withdraw_response = load_account.withdraw(amount)
                        if not withdraw_response:
                            #Insufficient funds
                            bt_view.get_post_withdrawal_reject_msg()
                        else:
                            #OLD
                            #bt_view.get_post_withdrawal_msg(amount)
                            bt_view.get_post_withdrawal_msg(amount, withdraw_response)
                    elif op2_selection == '3':
                        #Deposit
                        amount = bt_view.get_with_or_dep_amount("Deposit Amount:")
                        #OLD:
                        #new_balance = bt_model.deposit(account, amount)
                        #bt_view.get_post_deposit_msg(amount,new_balance)
                    
                        #NEW: Call instance method 'deposit' to add to bal for load_account object
                        bt_view.get_post_deposit_msg(amount, load_account.deposit(amount))                        
                    else:
                        #OLD
                        #bt_model.save()
                        
                        #NEW: Call Class method to save to json file 
                        oo_bt_model.Account.save_datafile()
                        return
        else:
            #OLD
            #bt_model.save()
                        
            #NEW: Call Class method to save to json file 
            oo_bt_model.Account.save_datafile()
            return

if __name__ == "__main__":
    run()