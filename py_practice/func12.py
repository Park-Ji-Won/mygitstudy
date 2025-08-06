#프랙털(fractal) 프로그램 예제
import turtle

def tree(length):
   if length > 5: #length가 5보다 크면 순환호출 실시
    t.fd(length) #거북이가 length만큼 선을 그림
    t.rt(20) #오른쪽으로 20도 회전
    tree(length-15) #(length-15)를 인수로 호출 tree()를 순환호출
    t.lt(40) #왼쪽으로 40도 회전
    tree(length-15) #(length-15)를 인수로 호출 tree()를 순환호출
    t.rt(20) #오른쪽으로 20도 회전
    t.backward(length) #length만큼 뒤로 간다. 제자리로 돌아온다.
    
t=turtle.Turtle()
t.lt(90) #거북이를 위쪽으로 향하게 한다.

t.color("green") #선의 색을 녹색으로 한다.
t.speed(5) #속도를 제일 느리게 한다.
tree(120) #길이 90으로 tree()를 호출

turtle.exitonclick()