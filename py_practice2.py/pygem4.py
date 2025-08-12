#if and else , elif and for 

age=40

if age>50:
    print("정년입니다.")
elif age>=40:
    print("곧 정년입니다.")
elif age>=30:
    print("아직 한창입니다")
else:
    print("더욱더 정진하세요.")
    
#리스트를 활용한 반복

fruits=['사과','바나나','용과','딸기']

for fruit in fruits:
    print(f"{fruit}를 섭취했습니다.")
    
my_human={"Name":"John","Age":"30","Favorite":"Seeking"}

for key in my_human:
    value = my_human[key]
    print(f"{key}:{value}")
