#디폴트 인수(default argument)
"""def greet(name,msg): #greet()는 항상 2개의 인수를 받아야함
    print("안녕", name+', '+msg)
    
greet("철수","좋은 아침!")#greet()함수에 두개의 인수를 전달하지 못하면 출력하지 못하는 오류가 발생
"""

#보완책
def greet(name,msg="별일 없죠?"): #인수가 부족할 경우 기본값을 넣어주는 메커니즘을 주면 편리함
    print("안녕 ", name+', '+msg)

greet("영희")
#이러한 방식이 디폴트 인수다

