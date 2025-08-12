#P-267
import turtle
import random
import math

player=turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
screen=player.getscreen()

asteroids=[]
for i in range(10):
    a1= turtle.Turtle()
    a1.color("red")
    a1.shape("circle")
    a1.penup()
    a1.speed(0)
    a1.goto(random.randint(-300,300), random.randint(-300,300))
    asteroids.append(a1)
    
def turnleft():
    player.left(30)

def turnright():
    player.right(30)
    
screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.listen()

def play():
    player.fd(2)
    for a in asteroids:
        a.right(random.randint(-180,180))
        a.fd(2)
    screen.ontimer(play,100)
screen.ontimer(play,100)
screen.mainloop()#바로 exit 되는거 방지