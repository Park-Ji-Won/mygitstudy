#리스트
fruits=["apple","peer","mango","greatfruits"]

mixed_list=[1,"너",True,3.14]

print(fruits)
print(mixed_list)

#슬라이싱
print(fruits[1:])
print(mixed_list[:4])

#값변경
fruits[2]='dragontooth'
print(f"값 변경후: {fruits}")

#맨뒤값추가
mixed_list.append("Billy")
print(f"값추가후: {mixed_list}")

#특정위치 값 삭제
del mixed_list[3:]
print(f"값 삭제 후:{mixed_list}")

#해당 리스트의 길이=> 데이터의 개수 구함
print(f"현재 해당 리스트의 길이:{len(fruits)}")
print(f"현재 해당 리스트의 길이:{len(mixed_list)}")