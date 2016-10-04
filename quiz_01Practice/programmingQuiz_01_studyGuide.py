#Kristen Ching
num = 45
print ("IronMan has", num, "kinds of weapons in his suit.")

pres = "Abraham Lincoln"
quote = "Whatever you are, be a good one."
#print(pres + " once said, " + '"Whatever you are, be a good one."')
print(pres + " once said, \"" + quote + "\"")

h = 45
w = 64
#area = h*w
#print ("The area of your rectangle is...", area)
print("The area of your rectangle is...", h*w)

#Question #4
#Because the vaiable slices was converted to an integer, but you can't put integers in print statements with other strings

#Question #5
#B

#Question #6
#B

#Question #7
#Because of the double quotes, it thinks "R. Kelly said " is a string and "I believe I can fly" is a variable.
print('R. Kelly said, "I believe I can fly!"')

print("This one goes on top\nThis one goes on bottom")

#print("a  b  c\nd  e  f\ng  h  i")
print("a\tb\tc\nd\te\tf\ng\th\ti")

#Question #10
#You have to convert the inputs to integers. They are automatically strings.
math = int(input("Please enter Math grade: "))
science = int(input("Please enter Science grade: "))
english = int(input("Please enter English grade: "))
history = int(input("Please enter History grade: "))
chemistry = int(input("Please enter Chemistry grade: "))
		
gpa = (math + science + english + history + chemistry)/500
gpa = str(gpa)
print (gpa)
