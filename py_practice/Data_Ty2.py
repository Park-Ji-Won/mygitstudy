import turtle
t=turtle.Turtle()
t.shape("classic")
size=int(input("크키를 입력하시오: "))

s=turtle.textinput("", "이름을 입력하시오: ")
t.write("안녕하세요?" + s +"씨, 터틀 인사드립니다.")

t.lt(90)
t.fd(size)
t.lt(90)
t.fd(size)
t.lt(90)
t.fd(size)
t.lt(90)
t.fd(size)

turtle.exitonclick()