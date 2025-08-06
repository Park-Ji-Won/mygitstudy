"""import turtle #터틀 그래픽 모듈을 포함한다

def draw(x,y):
    t.goto(x,y)

t=turtle.Turtle()
t.shape("turtle")
t.pensize(10)
s=turtle.Screen() #그림이 그려지는 화면을 얻음.
s.onscreenclick(draw) #마우스 클릭 이벤트 처리 함수를 등록

turtle.done()
"""

#수정본

import turtle

def draw(x,y):
    t.goto(x,y)
    
t=turtle.Turtle()
t.shape("turtle")
t.pensize(10)

s=turtle.Screen()
s.onscreenclick(draw)#마우스 클릭 이벤트 처림 함수를 등록한다.

s.onkey(t.penup,"Up")#위쪽 화살표키 이벤트를 처리하는 함수 등록
s.onkey(t.pendown,"Down")#아래쪽 화살표키 이벤트를 처리하는 함수 등록
s.listen()#키보드 이벤트를 기다림

turtle.done()