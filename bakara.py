# bakara simulator
import random
from bakara_tools import *

deck=DECK()
player_a=PLAYER(100)
player_b=PLAYER(100)
bank=BANK(100000)

player_list=[player_a,player_b]
p_side=[0,0]
b_side=[0,0]


while (len(player_list) >0) and bank.num_money()>0:
    bets={}
    for p in player_list:
        bets[p]=p.bet
        
    
    
    p_side[0]=CARD(deck.deal())
    b_side[0]=CARD(deck.deal())
    p_side[1]=CARD(deck.deal())
    b_side[1]=CARD(deck.deal())
    
    winner=solve(p_side,b_side, deck)
    
    
    
