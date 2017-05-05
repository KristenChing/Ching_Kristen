import turtle
wn = turtle.Screen()
wn.bgcolor("white")
            
move = turtle.Turtle()
move.color("darkgreen")
move.pensize(5)
move.speed(0)

def left():
    move.left(90)

def right():
    move.right(90)
turtle.listen()
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
while True:
    move.forward(2)

