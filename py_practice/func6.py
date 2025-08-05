def calculate_area (radious):
    result = 3.14*radious**2
    return result

r=float(input("원의 반지름: "))
area=calculate_area(r) #r,area는 calculate_area() 함수의 외부에서 생성된 전역변수(global variable)
#print(result) # result는 calculate_area()안에서만 사용가능한 지역변수(local variable)
print(area)