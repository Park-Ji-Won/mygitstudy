#콜백함수(callback function)
import turtle
t=turtle.Turtle()

"""삼각형을 그리는 함수를 정의"""
def square(length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
        
"""마우스가 클릭된 곳에 사각형을 그리는 함수를 정의"""        
def drawit(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.color("green")
    square(50)
    t.end_fill()
    
s=turtle.Screen()#그림이 그려지는 화면을 얻는다.
s.onscreenclick(drawit)#마우스 클릭 이벤트 처리 함수를 등록함.

turtle.done()