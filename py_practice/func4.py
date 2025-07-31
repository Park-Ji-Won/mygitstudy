import turtle

t=turtle.Turtle()
t.shape("turtle")

def square(length):#한변의 길이
    for i in range(4):
        t.fd(length)
        t.lt(90)

t.up()        
t.goto(-200,0)
t.down()
square(100);

t.up()        
t.goto(0,0)
t.down()
square(100);

t.up()        
t.goto(200,0)
t.down()
square(100);

turtle.exitonclick()