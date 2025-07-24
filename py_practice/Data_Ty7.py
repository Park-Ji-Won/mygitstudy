import turtle
t=turtle.Turtle()
t.shape("turtle")

x=[]
y=[]

for i in range(3):
    xi=int(input(f"x{i+1} : "))
    yi=int(input(f"y{i+1} : "))
    x.append(xi)
    y.append(yi)

t.penup
t.goto(0,0)
t.pendown()    

t.goto(x[0],y[0])
t.goto(x[1],y[1])
t.goto(x[2],y[2])

turtle.exitonclick()