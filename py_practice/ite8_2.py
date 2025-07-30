total=0
answer="no"
while answer=="yes":#변수가 answer가 yes인지 검사=>참일경우 반복 계속
    number=int(input("숫자를 입력하시오: "))
    total=total+number
    answer=input("계속?(yes/no): ")
print("합계는 : ",total)#조건이 거짓이라면 다음 단계로 이동