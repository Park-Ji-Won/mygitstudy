heroes=['iron man','Thor','Hulk','Scarlet Witch']
heroes.sort()#리스트안의 항목들을 크기순으로 나열 #원래 리스트만 변경
print(heroes)#리스트안에는 문자열이 있어 알파벳순으로 나열됨

numbers=[9,6,7,10,54,15,1,3,7,4]
numbers.sort()
print(numbers)#리스트안에 있는 숫자 크기순으로 나열

new_list=sorted(numbers)#sorted 정렬된 새로운 리스트를 반환
print(new_list)

new_list2=sorted(numbers,reverse=True)#리스트를 역으로 정렬
print(new_list2)