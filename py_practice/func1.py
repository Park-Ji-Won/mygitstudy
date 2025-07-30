def print_address(): # def키워드를 사용한 함수정의 #:=>코드블록 등장
    print("강원특별자치도 원주시 교동 45번지")
    print("Monty Python 본사")
    print("허셸 폰 클라우스 슈타우펜베르크")
    #함수를 구성하는 문장들 들여쓰기 필수

print_address()#정의 해당 함수 호출

def print_address(name):#변수 name이 해당 변수를 통하여 함수로 값이 전달된다/(매개변수[parameter])
    print("강원특별자치도 원주시 교동 45번지")
    print("Monty Python 본사")
    print(name)#전달받는 해당 변수 

print_address("허셸 폰 클라우스 슈타우펜베르크")#전달되는 해당 값/(인수[argument])
    