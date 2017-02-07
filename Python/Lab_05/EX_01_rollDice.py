#Kristen Ching
import random
yourRoll = random.randint(1,6)
compRoll = random.randint(1,6)

def rollDice(roll_1, roll_2):
    if roll_1 > roll_2:
        return "you"
    elif roll_1 < roll_2:
        return "computer"
    elif roll_1 == roll_2:
        return "nobody"

winner = rollDice(yourRoll, compRoll)
print ("You rolled a", yourRoll)
print ("Computer rolled a", compRoll)
if winner == "nobody":
    print ("You and computer tied.")
else:
    print ("Winner is", winner)
    
