import random

class DECK:
    def __init__(self,num_deck,burn_num):
        self.num_card=num_deck*52
        self.card_list=list(range(self.num_card))
        for i in range(burn_num):
            self.card_list.pop(random.choice(self.card_list)-1)
    def num_cards(self):
        return len(self.card_list)
        
    def deal(self):
        return self.card_list.pop(random.choice(self.card_list)-1)
    
def CARD(num):
    temp_num=(num%13)
    if temp_num == 0:
        temp_num=13
    return max(temp_num,10)


class PLAYER:
    def __init__(self, money):
        self.money=money
    def bet(self, bef,signal):
        return 10,signal
    def num_money(self):
        return self.money
    def add_money(self,mon):
        self.money+=mon
    def sub_money(self,mon):
        self.money-=mon
    
class BANK:
    def __init__(self, money):
        self.b_money=money
    def num_money(self):
        return self.money
    def add_money(self,mon):
        self.b_money+=mon
    def sub_money(self,mon):
        self.b_money-=mon
        
        
def solve(p_side, b_side, deck):
    p_num=sum(p_side)%10
    b_num=sum(b_side)%10
    #true is player side
    
    if (p_num == 8) or (b_num ==8 ) or (p_num==9) or (b_num == 9):
        if p_num>b_num:
            return 'p'
        elif p_num==b_num:
            return 't'
        else:
            return 'b'
    elif (p_num==6) or (p_num==7):
        if(b_num<=5):
            b_num=(b_num+CARD(deck.deal()))%10
        if p_num>b_num:
            return 'p'
        elif p_num==b_num:
            return 't'
        else:
            return 'b'
        
        
        
    p_num<=5:
        p_num=(p_num+CARD(deck.deal()))%10

        







        