n=int(input("정수를 입력하시오 : "))
n1=n % 10 # 나머지
n2=n // 10 # 몫
n3=n2 % 10
n4=n2 // 10
n5=n4 % 10
n6=n4 // 10

sum=n1+n3+n5+n6

weight=int(input("물체의 무게를 입력하시오(kg): "))
speed=int(input("물체의 속도를 입력하시오(m/s): "))

energy=1/2*weight*speed**2

print("자리수의 합: ",sum)

print("물체는", energy, "(줄)의 에너지를 가지고 있다.")
