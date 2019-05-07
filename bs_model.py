from random import randint

class Gameboard:

    #Class attributes
    
    #def __init__(self, rows_list=[], ship_row="", ship_col=""):
    def __init__(self):
        # populate self.attributes for a bank account
        self.rows_list = []
        self.ship_row = randint(1,5)
        self.ship_col = randint(1,5)
        print("Ship row = ", self.ship_row, ", Ship col = ", self.ship_col)
        for i in range(5):
            self.rows_list.append("-" * 5)

    def attack(self, attack_row, attack_col):
        self.attack_row = int(attack_row)
        self.attack_col = int(attack_col)
        
        if self.attack_row == self.ship_row and self.attack_col \
        == self.ship_col:
            return True
        else:
            row_str = self.rows_list[self.attack_row-1]
            pre_row_str = row_str[:self.attack_col-1] 
            post_row_str = row_str[self.attack_col:]
            self.rows_list[self.attack_row-1] = pre_row_str+"x"+post_row_str
            return self.rows_list



