import turtle
t=turtle.Turtle()
t.shape("turtle")
t.width(5)
t.shapesize(3,3)

for count in range(6): #range(6)호출=>여섯개의 숫자[0,1,2,3,4,5]생성
    t.circle(200)#반지름이 200인 원
    t.lt(360/6)#커서를 360 / 6 = 60도 만큼 회전시킨다

turtle.exitonclick()