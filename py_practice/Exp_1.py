X=int(input(""))
Y=int(input(""))
big=max(X,Y) #큰수를 나타내는 함수
small=min(X,Y) #작은수를 나타내는 함수

print("두수의 합:",X+Y)
print("두수의 차:",X-Y)
print("두수의 곱:",X*Y)
print("두수의 평균:",(X+Y)//2)
print("큰 수: ",big)
print("작은 수: ",small)

r=10
h=100
vol=3.14*r**2 *h #pai* r제곱2 *h

print("원기둥의 부피: ", vol)