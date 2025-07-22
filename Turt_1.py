import turtle
t=turtle.Turtle()
t.shape("square") #변경가능(arrow,turtle,circle,square,triangle,classic)

t.width(5) #선의 굵기 
t.fd(150)
t.lt(60)
t.fd(150)
t.lt(60)
t.fd(150)
t.lt(60)
t.fd(150)
t.lt(60)
t.fd(150)
t.lt(60)
t.fd(150)

t.circle(130) #반지름이 130
t.bk(100)
t.circle(130)

t.bk(100)
t.fd(90)
t.rt(90)
t.fd(90)
t.rt(90)
t.fd(90)
t.rt(90)
t.fd(90)
t.rt(90)

t.up()# 펜올려라
t.goto(100,200) #해당좌표로 이동하라(0,0)이 기준
t.down()

t.circle(200)

turtle.exitonclick() #결과창 클릭하는 순간 꺼짐

