n=input("정수를 입력하시오: ").strip()
total =sum(int(d) for d in n if d.isdigit())
print("자리수의 합: ",total)
