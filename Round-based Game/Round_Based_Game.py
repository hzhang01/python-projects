# GOAL
# Write a simple game that allows the user and the computer to take turns selecting moves to use against each other. 
#Both the computer and the player should start out at the same amount of health (such as 100), and should be able to choose between the three moves:
# The first move should do moderate damage and has a small range (such as 18-25).
# The second move should have a large range of damage and can deal high or low damage (such as 10-35).
# The third move should heal whoever casts it a moderate amount, similar to the first move.
# After each move, a message should be printed out that tells the user what just happened, and how much health the user and computer have. 
#Once the user or the computer's health reaches 0, the game should end.
# SUBGOALS
# When someone is defeated, make sure the game prints out that their health has reached 0, and not a negative number.
# When the computer's health reaches a set amount (such as 35%), increase it's chance to cast heal.
# Give each move a name.

import random

class Player(object):
    """ This class defines each player's health condition and attack moves"""
    health = 100
    
    def __init__(self,name):
        self.name = name

    def weak_move(self,opponent):
        """ This method defines the damage and how it is inflicted by a weak move"""
        damage = random.randint(-27,-15)
        opponent.health += damage
        return damage
        
    def strong_move(self,opponent):
        """ This method defines the damage and how it is inflicted by a strong move"""
        damage = random.randint(-35,-10)
        opponent.health += damage
        return damage
        
    def heal_move(self):
        """ This method defines the healing amount by a healing move"""
        heal = random.randint(18,25)
        
        # If healing will not make health exceed 100 HP
        if (self.health + heal <= 100):
            self.health += heal
            return heal
            
        # if it does exceed return 0 healing amount 
        else:
            self.health = 100
            return 0
            
    def is_alive(self):
        """ This method idicates the aliveness of a player"""
        
        # If a player's health is less and equal to 0, then the play is dead
        if self.health <= 0:
            return False
        
        # Otherwise the player is alive
        return True

"""Game Interface"""

print ("Wecome to the Fake Pokemon game!")
print ("This is a round based game with your nemesis!")
print ""
name = raw_input("Please enter your name: ")
nem = raw_input("Please enter your nemesis' name: ")
user = Player(name)
comp = Player(nem)

print("")

print "%s, the battle begins!\n" % (user.name)

"""While both players are alive"""
while ((user.is_alive() == True)  & (comp.is_alive() == True)):
    
    # Showing to the user about each player's health and available moves 
    print "Health: %s - " % (user.name) + str(user.health) + "  %s - " % (comp.name) + str(comp.health)
    print ("Moves:\tTackle (t) \n\tDouble-Edge (d) \n\tHeal (h)\n")
    choice = raw_input("Which move do you want to use?")

    # Validating the move choice, if invalid reprompt the user
    while(choice.lower() not in "tdh"):
        print "Please enter a valid move!\n"
        choice = raw_input("Which move do you want to use?")
    
    print ""
    
    # Processing a valid move choice by applying the damage counter
    hp_change1 = 0
    
    # If the choice is (t)ackle 
    if(choice.lower() == "t"):
        hp_change1 = user.weak_move(comp)
        
    # If the choice is (d)ouble-edge
    elif(choice.lower() == "d"):
        hp_change1 = user.strong_move(comp)
    
    # If the choice is (h)eal
    else:
        hp_change1 = user.heal_move()      
    
    # Printing the damage 
    # If damage was infliced 
    if (hp_change1 < 0):
        print ("%s inflictes %dHP of damage!") % (user.name,-hp_change1)
    
    # If health is full while healing 
    elif(hp_change1 == 0):
        print ("%s's health is full!") % (user.name)
        
    # If healing succeeds 
    else:
        print ("%s recovers %dHP!") % (user.name,hp_change1)
    
    # Processing nemesis's choice (computer)
    print ""
    choice = 0
    hp_change2 = 0
    
    # If the the nemesis is healthy (above 35% of health)
    if (comp.health > 35):
        choice = random.randint(0,2)
        
        # If nemesis uses the weak move
        if choice == 0:
            hp_change2 = comp.weak_move(user)
            
        # If nemesis uses the strong move
        elif choice == 1:
            hp_change2=comp.strong_move(user)
        
        # If the nemesis uses the healing move
        else:
            hp_change2 = comp.heal_move()
            
    # If nemesis's health is below 35% 
    else:
        choice = random.randint(0,3)
        hp_change2 = 0
        
        if choice == 0:
            hp_change2 = comp.weak_move(user)
        
        elif choice == 1:
            hp_change2=comp.strong_move(user)
        
        #The nemesis is more likely to heal than to attack
        else:
            hp_change2 = comp.heal_move()
    
    # Print nemesis' decision and associated damage
    if choice == 0:
        print "%s inflicts %dHP of damage with Tackle!" % (comp.name, -hp_change2)
    elif choice == 1:
        print "%s inflictes %dHP of damage with a Double-Edge!" % (comp.name, -hp_change2)
    else:
        print "%s heals for %dHP!" % (comp.name, hp_change2)
    
    print ""
    
# If nemesis wins
if (comp.is_alive()):
    print "You lost..."
    print "Game Over!"
    
# If user wins 
else:
    print "You Won!"
    
print "Thank you for playing! See you next time!"
    
        
    