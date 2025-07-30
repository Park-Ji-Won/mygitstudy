import random

x1=max(random.randint(1,100),random.randint(1,100))
x2=min(random.randint(1,100),random.randint(1,100))

correct_answer= x1 - x2

user_answer=int(input("문제 :" +str(x1)+"-"+str(x2)+" = ? "))

if user_answer == correct_answer:
    print("맞았습니다.")
else:
    print("틀렸습니다 ")