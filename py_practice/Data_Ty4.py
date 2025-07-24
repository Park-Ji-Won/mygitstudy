import turtle
t=turtle.Turtle()
t.shape("classic")

color_list=["blue","yellow","red","gray"]#리스트를 사용해 색상 저장

t.fillcolor(color_list[0]) #저장된 리스트의 색상 설정
t.begin_fill() #설정된 리스트의 색상으로 채우기 시작
t.circle(100) #해당 색이 채워진 원이 해당 반지름 수치만큼의 크기로 그려짐
t.end_fill() #색상 채우기를 종료

t.fd(100)
t.fillcolor(color_list[1])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(100)
t.fillcolor(color_list[2])
t.begin_fill()
t.circle(100)
t.end_fill()

t.fd(100)
t.fillcolor(color_list[3])
t.begin_fill()
t.circle(100)
t.end_fill()

turtle.exitonclick()