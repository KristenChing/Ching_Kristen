import turtle
import time
wn = turtle.Screen()
wn.bgcolor("white")
snake = turtle.Turtle()
snake.color("darkgreen")
snake.pensize(5)
snake.speed(0)
snake.hideturtle()
snaketail = turtle.Turtle()
snaketail.color("white")
snaketail.pensize(5)
snaketail.speed(0)
snaketail.hideturtle()
coords = []
turns = 0
#stTurns = 1
speed = 1
oldx = 0
oldy = 0
oldoldx = 0
oldoldy = 0
turnedLeft = False
turnedRight = False
timer = 5
def addspeed():
    global speed
    speed = 2
def resetcoords():
    global x
##    global oldx
##    global oldoldx
    x = snake.xcor()
##    oldoldx = oldx
##    oldx = x 
    global y
##    global oldy
##    global oldoldy
    y = snake.ycor()
##    oldoldy = oldy
##    oldy = y
    coords.append([])
    coords[turns - 1].append(x)
    coords[turns - 1].append(y)
def left():
    global turnedLeft
    global turns
    turns += 1
    snake.left(90)
    resetcoords()
    turnedLeft = True
def right():
    global turnedRight
    global turns
    turns += 1
    snake.right(90)
    resetcoords()
    turnedRight = True
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
while True:
    snake.forward(2)
    snaketail.forward(speed)
    x = snake.xcor()
    y = snake.ycor()
    print("turns", turns)
    print("coords list", coords)
    print("snake coords", snake.xcor(), snake.ycor()) 
    print("snaketail coords", snaketail.xcor(), snaketail.ycor())
    print("\n")
    for x in range(turns):
        if (snaketail.xcor() == coords[x][0]) and (snaketail.ycor() == coords[x][1]):
            if turnedLeft == True:
                snaketail.left(90)
                addspeed()
                turnedLeft = False
                #stTurns += 1
            if turnedRight == True:
                snaketail.right(90)
                addspeed()
                turnedRight = False
                #stTurns += 1
##    if (snaketail.xcor() == oldx) and (snaketail.ycor() == oldy):
##        if turnedLeft == True:
##            snaketail.left(90)
##            addspeed()
##            turnedLeft = False
##        if turnedRight == True:
##            snaketail.right(90)
##            addspeed()
##            turnedRight = False
##    if (snaketail.xcor() == oldoldx) and (snaketail.ycor() == oldoldy):
##        if turnedLeft == True:
##            snaketail.left(90)
##            addspeed()
##            turnedLeft = False
##        if turnedRight == True:
##            snaketail.right(90)
##            addspeed()
##            turnedRight = False


#-------------------------------------debug code-------------------------------
#print("oldx", oldx)
#print("oldy", oldy)
#print(x)
#print(y)
#print("tailx", snaketail.xcor())
#print("taily", snaketail.ycor())
#print("oldoldx", oldoldx)
#print("oldoldy", oldoldy)
#print("\n")


