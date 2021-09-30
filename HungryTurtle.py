import turtle
import random
import math
import time
from random import uniform

# create screen
win = turtle.Screen()
win.title('Hungry Turtle')
win.bgcolor('lightpink')
win.tracer(3)

# instructions for game

instructions = turtle.Turtle()
instructions.color('white')
instructions.penup()
instructions.hideturtle()
instructions.setposition(-300, 260)
welcome = "INSTRUCTIONS:\nUse your keyboard arrows and chase the dots for points.\nPress up/down to adjust speed."
instructions.write(welcome, align = 'left', font = ('Futura', 14, 'bold'))

title = turtle.Turtle()
title.color('white')
title.penup()
title.hideturtle()
titlePresent = "Hungry Turtle Game"
title.write(titlePresent, align = 'center', font = ('Futura', 50, 'bold'))

start = turtle.Turtle()
start.color('white')
start.penup()
start.hideturtle()
start.setposition(290, -300)
startPrint = "Game begins in 5 seconds"
start.write(startPrint, align = 'right', font = ('Futura', 20, 'bold', 'underline'))

time.sleep(5)

title.undo()
title.hideturtle()
instructions.undo()
instructions.hideturtle()
start.undo()
start.hideturtle()

# create border so objects don't fly away forever
border = turtle.Turtle()
border.color('white')
border.hideturtle()
border.speed('fastest')
border.penup()
border.setposition(-300, -300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()

# create turtle (player)
player = turtle.Turtle()
player.color("black")
player.shape('turtle')
player.penup()

# create food for turtle
maxFood = 5
food = []

for count in range(maxFood):
    food.append(turtle.Turtle())
    food[count].shape("circle")
    food[count].color("red")
    food[count].penup()
    food[count].speed(0)
    food[count].shapesize(0.5, 0.5)
    food[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

# set speed variable
speed = 1

# define function
def turnleft():
    player.left(25)
def turnright():
    player.right(25)
def increasespeed():
    global speed
    speed += 2
def decreasespeed():
    global speed
    speed -= 2

def win(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

# score
score = 0
    
# set keyboard bindings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)

    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)

    for count in range(maxFood):
        food[count].forward(3)
    
        if food[count].xcor() > 270 or food[count].xcor() < -270:
            food[count].right(180)
        if food[count].ycor() > 270 or food[count].ycor() < -270:
            food[count].right(180)

        if win(player, food[count]):
            food[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            food[count].right(random.randint(0, 360))
            score += 1
            border.undo()
            border.penup()
            border.setposition(-300, 310)
            printScore = "Score: %s" %score
            border.write(printScore, False, align = 'left', font = ('Ariel', 14, 'bold'))

delay = input("Press Enter to exit.")
