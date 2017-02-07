#Kristen Ching 
name = input("What is your name? ")
print (name + "!?!?! That's the worst name I've ever heard! Wow, do I feel sorry for you.")
age = int(input("How old are you, " + name + "? " + "(Please enter an integer)"))
if age <= 15:
    age = str(age)
    print ("Whoa, you're " + age + "!? That's so YOUNG!!!! Grow up faster, will ya?")
elif (age > 15) and (age < 30):
    age = str(age)
    print (age + "!? Gaaah, you're getting old!!!")
elif age > 30:
    age = str(age)
    print ("You're " + age + "!? You're really THAT OLD???")
fun = input("What do you do for fun, " + name + "? ")
print (fun + "!? That doesn't sound fun to me!")
music = input("What kind of music do you like? ")
print ("Eww, I hate " + music + " music!!!")
siblings = input("How many siblings do you have? (Please enter an integer) ")
print (siblings + "? Ha, that must be hard.")
job = input("What do you want to be when you grow up? ")
print ("I think you're too dumb to become a(n) " + job)
print ("So " + name + ", you're " + age + "...\nYou like to " + fun + " and listen to " + music + "...\nGood luck becoming a(n) " + job + ".\nI'm only kidding, " + name + ".")
