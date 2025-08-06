import random
import turtle

#(x,y)위치에 미로를 그린다.
def draw_maze(x,y):
    for i in range(2):
        t.penup()
        if i==1:
            t.goto(x+100,y+100)
        else:
            t.goto(x,y)
        t.pendown()
        t.fd(300)
        t.rt(90)
        t.fd(300)
        t.lt(90)
        t.fd(300)

#turtle을 왼쪽으로 회전하여 10만큼 전진
def turn_left():
    t.lt(10)
    t.fd(10)
    
#turtle을 오른쪽으로 회전하여 10만큼 전진
def turn_right():
    t.rt(10)
    t.fd(10)
    
t=turtle.Turtle()
screen=turtle.Screen()
t.shape("turtle")
t.speed(5)

draw_maze(-300,200)
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")

t.penup();
t.goto(-300,200)
t.speed(2)
t.pendown();
screen.listen()
screen.mainloop()