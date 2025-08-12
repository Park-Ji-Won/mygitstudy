#딕셔너리
my_human_info={
    "Name":"John",
    "Age":29,
    "City":"Tokyo",
    "Favorite" : ["apple","corn","ice_cream"] 
}

print(my_human_info)

#키값을 이용=> 접근,호출
print(f"이름:{my_human_info['Name']}")

#값수정
my_human_info["Age"]=39
print(f"수정된 나이:{my_human_info['Age']}")

#새로운 키-값 쌍 추가
my_human_info['Status']='Anlyist'
print(f"추가 후 새로운 정보:{my_human_info}")

#키-값 쌍 삭제
del my_human_info["Age"]
print(f"삭제 후 정보: {my_human_info}")