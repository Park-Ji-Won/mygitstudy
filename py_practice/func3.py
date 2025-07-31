def get_sum(start,end):#매개변수
    sum=0
    for i in range(start,end+1):
        sum += i
    return sum

print(get_sum(1,10))#print(인수)

#주의 매개변수의 개수는 정확히 인수에 맞춰서 일치해야 한다 
#EX)매개변수가 두개 따라서 인수도 두개
#해당 문제를 그대로 방치하고 지나간다면 아주 찾기 어려운 오류가 발생