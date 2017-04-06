# Author: Han Zhang
# Creating a Black Jack game played between the user and the computer. 
# The cards are removed from the pile after dealing.
# User plays first until either stand, bust or win.
# Then computer plays if the user chooses to stand.

import random

cards_com = cards = ['10 of Hearts', '9 of Hearts', '8 of Hearts', 
                    '7 of Hearts', '6 of Hearts', '5 of Hearts', 
                    '4 of Hearts', '3 of Hearts', '2 of Hearts', 
                    'Ace of Hearts', 'King of Hearts', 'Queen of Hearts', 
                    'Jack of Hearts', '10 of Diamonds', '9 of Diamonds', 
                    '8 of Diamonds', '7 of Diamonds', '6 of Diamonds', 
                    '5 of Diamonds', '4 of Diamonds', '3 of Diamonds', 
                    '2 of Diamonds', 'Ace of Diamonds', 'King of Diamonds', 
                    'Queen of Diamonds', 'Jack of Diamonds', '10 of Clubs', 
                    '9 of Clubs', '8 of Clubs', '7 of Clubs', '6 of Clubs', 
                    '5 of Clubs', '4 of Clubs', '3 of Clubs', '2 of Clubs', 
                    'Ace of Clubs', 'King of Clubs', 'Queen of Clubs', 
                    'Jack of Clubs', '10 of Spades', '9 of Spades', 
                    '8 of Spades', '7 of Spades', '6 of Spades', 
                    '5 of Spades', '4 of Spades', '3 of Spades', 
                    '2 of Spades', 'Ace of Spades', 'King of Spades', 
                    'Queen of Spades', 'Jack of Spades']

values_com = values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 
                       10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 
                       10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10, 
		       10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 10, 10]

# Returning the card name
# arugments: integer idx in list x
#	     list x stores the names
# return: card name

def card_name(idx,x):
    cardname = x[idx]
    x.remove(x[idx])
    return cardname

# Returning the card value
# aruments: integer idx in list x
#	    list x stores the values
# return: card value

def card_value(idx,x):
    cardvalue = x[idx]
    x.remove(x[idx])
    return cardvalue

# Main program
    
def main():
    
    hand = []
    handvalue = 0

    # Initializing the game by dealing two cards
    c1 = random.randint(0,len(cards)-len(hand))
    cd = card_name(c1,cards)
    hand.append(cd)
    cdv = card_value(c1,values)
    handvalue += cdv
    
    c2 = random.randint(0,len(cards)-len(hand))
    cd = card_name(c2,cards)
    hand.append(cd)
    cdv = card_value(c2,values)
    handvalue += cdv
    
    print("Player hand: ", hand, " is worth ", handvalue)
    choice = input("(h)it or (s)tand? ")
    
    end = False
    while choice != "s" and not end:
        if choice=="h":
            cn = random.randint(0,len(cards)-len(hand))
            cd = card_name(cn,cards)
            hand.append(cd)
            cdv = card_value(cn,values)
            handvalue += cdv
            
            print("You drew",cd)
            print("Player hand:", hand, "is worth", handvalue)
            if handvalue > 21:
                print("Bust!")
                print("Computer Wins")
                end=True
            elif handvalue == 21:
                print("You got 21! Blackjack!")
                print("Player Wins")
                end=True
            else:
                choice=input("(h)it or (s)tand? ")

    # End of user's round, initiate computer's hand            
    if not end:
        hand_com = []
        handvalue_com = 0
        c11 = random.randint(0,len(cards_com)-len(hand))
        cd = card_name(c11,cards_com)
        hand_com.append(cd)
        cdv = card_value(c11,values_com)
        handvalue_com += cdv
        
        c21 = random.randint(0,len(cards_com)-len(hand))
        cd = card_name(c21,cards_com)
        hand_com.append(cd)
        cdv = card_value(c21,values_com)
        handvalue_com += cdv
        print("Computer hand:",hand_com,"is worth",handvalue_com)
        
        while not end:
            c31 = random.randint(0,len(cards_com)-len(hand))
            cd = card_name(c31,cards_com)
            hand_com.append(cd)
            cdv = card_value(c31,values_com)
            handvalue_com += cdv
            print("Computer drew",cd)
            print("Computer hand:",hand,"is worth",handvalue_com)
            
            if handvalue_com>21:
                print("Bust!")
                print("Player Wins")
                end=True
            elif handvalue_com==21:
                print("You got 21! Blackjack!")
                print("Computer Wins")
                end=True
            else:
                end=False
                
main()
