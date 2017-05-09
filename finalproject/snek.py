import turtle
import time
turnLeft = False
turnRight = False
wn = turtle.Screen()
wn.bgcolor("white")

snake = turtle.Turtle()
snake.color("darkgreen")
snake.pensize(5)
snake.speed(0)
snake.hideturtle()
snaketail = turtle.Turtle()
snaketail.color("blue")
snaketail.pensize(5)
snaketail.speed(0)
snaketail.hideturtle()
##def follow(snake, snaketail):
##    x = snake.xcor()
##    y = snake.ycor()
##    time.sleep(5)
##    snaketail.goto(x, y)
##
oldx = 0
oldy = 0
def resetx():
    global x
    global oldx
    x = snake.xcor()
    oldx = x
def resety():
    global y
    global oldy
    y = snake.ycor()
    oldy = y
def left():
    snake.left(90)
    resetx()
    resety()
def right():
    snake.right(90)
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
while True:
    snake.forward(1.25)
    snaketail.forward(1)
    x = snake.xcor()
    y = snake.ycor()
    #print("oldx", oldx)
    #print("oldy", oldy)
    #print(x)
    #print(y)
    #print("tailx", snaketail.xcor())
    #print("taily", snaketail.ycor())
    #print("\n")
    if (snaketail.xcor() == oldx) and (snaketail.ycor() == oldy):
        if (y > oldy):
            snaketail.left(90)
        else:
            snaketail.right(90)
    #print(left())
    #if snaketail.xcor() != snake.xcor():
        #snaketail.goto(snake.xcor()- 100, snaketail.ycor())
    #if snake.ycor() > snaketail.ycor() and snake.xcor() != snaketail.xcor():
        #snaketail.left(90)
        #snaketail.goto(snake.xcor(), snake.ycor())
        #snaketail.pendown()
    #checkpos(x,y)
#def checkpos(x, y):
    #time.sleep(5)
    

    


