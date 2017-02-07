#Kristen Ching
#Sorry I like to import time, it's a fun element to add to story type programs.
import time
choice = input("School just ended. You are walking home when you spot a bowl of candies on the \nground. The bowl has a note on it that says, \"" + "Take one." + "\" Take a candy? Y/N ")
if choice == "Y":
     choice = input("How many candies are you going to take? A. 1 B.2 ")
     if choice == "A":
          print("You took one candy and continued down the road to your house.")
          time.sleep(1)
          choice = input("You arrive at home but the gate in front of your house is locked, and you don't have the keys. What do you do? A. eat the candy B. try to squeeze the candy into the lock ")
          if choice == "A":
               print("You ate the candy.")
               time.sleep(1)
               print("Nothing seems to be happening...")
               time.sleep(1)
               print("...")
               time.sleep(1)
               print ("...")
               time.sleep(1)
               print ("Did you win?")
          else:
               if choice == "asdfghjkl;":
                    print("You cut the candy into five pieces,")
                    time.sleep(1)
                    print("ate the first piece,")
                    time.sleep(1)
                    print("put the second piece in the lock,")
                    time.sleep(1)
                    print("molded the third piece into a key,")
                    time.sleep(1)
                    print("smashed the fourth piece into smithereens,")
                    time.sleep(1)
                    print("and stuck the fifth piece on the gate.")
                    time.sleep(1)
                    print("The gate opened...")
                    time.sleep(10)
                    print("Shhhh... secret ending!")
               else:
                    print("You tried to fit the candy into the lock...")
                    time.sleep(1)
                    print("It doesn't fit...")
                    time.sleep(1)
                    print("Did you win?")
     else:
          choice = input("You are almost at your house when you approach a boy who asks you how many candies you took. How do you reply? A. 1 B. 2 ")
          if choice == "A":
               print ("Congratulations, liar. You lost the game. >:D")
          else:
               print ("The boy allows you to pass. When you get home you realize that the other candy has disappeared...")
               time.sleep(1)
               print("You lost the game.")
else:
     choice = input("You arrive at home but the gate in front of your house is locked, and you don't have the keys. What do you do? A. try to climb over it B. cry out for help ")
     if choice == "A":
          print ("You tried to climb over the gate, but when you got to the top you felt like there was an invisible wall there and fell off. Now what? A. keep trying B. run back to the bowl to get a candy ")
          if choice == "A":
               print("You kept trying but that still didn't work...")
               time.sleep(1)
               print("You lost the game.")
          else:
               print ("You ran back to where the bowl had been but it was no longer there...")
               time.sleep(1)
               print("You lost the game.")
     else:
          choice = input("You called out for help but nobody came. Now what? A. keep trying B. give up ")
          if choice == "A":
               print ("Nobody has heard you...")
               time.sleep(1)
               print ("You lost the game.")
          else:
               print ("You gave up.")
               time.sleep(1)
               print ("You lost the game.")
