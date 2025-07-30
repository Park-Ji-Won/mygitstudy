#함수로 되돌아 오는 값=> 반환값
def calculate_area(radious):
    area=3.14*radious**2#원의 면적계산 = 3.14*반지름**2(지수)
    return area #해당 변수값을 calculate_area() 함수를 호출한 곳으로 반환한다

c_area=calculate_area(5.0) #c_area=3.14*5.0**2

print(c_area)#계산을 통해 해당값 저장

area_sum=calculate_area(5.0)+calculate_area(10.0) #area_sum=3.14*10.0**2

print(area_sum)