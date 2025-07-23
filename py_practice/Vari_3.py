first=int(input("첫번째 숫자를 입력하시오: "))
second=int(input("두번째 숫자를 입력하시오: "))
third=int(input("세번째 숫자를 입력하시오: "))
sum=first+second+third/3 #평균내기

radious=int(input("원의 반지름을 입력하시오: "))
circle=3.14*radious*radious # 3.14 X 반지름 X 반지름

name=input("이름을 입력하시오: ")
age=int(input("나이를 입력하시오: "))
furture=2020+(100-age)

print( name,"씨는", furture, "에 100살이시네요!")

print(first,second,third,"의 평균은",sum,"입니다,")

print("반지름이",radious,"인 원의 넓이 = ",circle)