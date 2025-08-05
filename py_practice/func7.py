"""def calculate_area(radious):
    area=3.14*radious**2 #전역변수 area에 계산값을 저장하려고 함 
    return  그러나 Python에서는 함수안에 변수에 값을 저장하면 새로운 지역변수로 생성하는 원리에
               따라 claculate_area()속 변수 area는 지역변수로 생성되지 전역변수로 생성되지 않는다.
area=0
r=float(input("원의 반지름: "))
calculate_area(r)
print(area)
"""
#수정안

def calculate_area(radius):
    global area #이때 global 이라는 키워드를 사용해 area변수를 전역변수로 지정해준다
    area = 3.14*radius**2
    return

area=0
r=float(input("원의 반지름: "))
calculate_area(r)
print(area)