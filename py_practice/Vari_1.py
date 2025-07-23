import turtle
t=turtle.Turtle()
t.shape("arrow")

size=int(input("집의 크기는 어느정도 바라십니까?: "))

t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)

t.rt(90)

t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)

turtle.exitonclick()