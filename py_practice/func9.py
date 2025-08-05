#키워드 인수(keyword Argument)
def calc(x,y,z):
    return x+y+z
#키워드 인수는 인수들 앞에 키워드 두어 인수들을 구별

r=calc(10,20,30)
print(r)

#위치인수(positional argument)
a=calc(x=10,y=20,z=30)
print(a)

#인수의 위치가 매개변수와 달라도 키워드 인수를 사용시 인수들이 어떤 순서 전달되어도 문제가 없다
b=calc(y=20,x=10,z=30)
print(b)

#위치인수와 키워드 인수는 섞여도 되지만 위치인수가 키워드 인수보단 앞이어야 한다
c=calc(10,y=20,z=30)
print(c)

#잘못된 예
#f=calc(x=10,20,30)
#print(f)