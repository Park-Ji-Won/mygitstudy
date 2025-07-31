import turtle
t=turtle.Turtle()
t.shape("classic")
t.speed(5)#커서 속도
t.color("red")#커서 색
t.pensize(2)#커서 사이즈

def n_polygon(n,length):
    for i in range(n):
        t.fd(length)
        t.lt(360//n)
        
for i in range(10):
    t.lt(20)
    n_polygon(6,100)
    
turtle.exitonclick()