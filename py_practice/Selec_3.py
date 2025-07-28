import turtle 
t=turtle.Turtle()
t.shape("turtle")
t.width(3)#선 굵기
t.shapesize(3,3) #커서 크기

while True:
    command=input("명령을 입력하시오.: ")
    if command == "l":
        t.lt(90)
        t.fd(100)
    if command == "r":
        t.rt(90)
        t.fd(100)
    if command == "quit":
        break # 루프 종료

turtle.exitonclick()