heroes=['homelander','blackwarrier','deep','mave','speeder','star']

heroes[1]= 'doctorstrager'#리스트에서 해당 인덱스 지정된 항목 변경
print(heroes)

heroes.append('spider')#리스트에 새롭게 항목 추가
print(heroes)

heroes.insert(1,'superman')#해당 인덱스 위치에 항목 아이템 추가 여기선 리스트의 중간에 추가
print(heroes)

heroes.remove('deep')#리스트에서 지정된 항목 삭제
print(heroes)

if 'homelander' in heroes:
    heroes.remove('homelander')#in 연산자와 if문을 활용하여 제거 
print(heroes)

del heroes[0]#해당 리스트의 인덱스를 활용하여 항목제거
print(heroes)

last_hero=heroes.pop()#리스트에서 마지막 항목을 지우고 반환
print(last_hero)
print(heroes)

print(heroes.index('mave'))#해당 특정항목이 리스트의 어떤 인덱스에 위치한지 확인하여 출력

if 'spider' in heroes:
    print(heroes.index('spider'))#탐색하기전 해당 항목이 리스트에 없어 출력에 오류가 날수있기에
                                #if문과 in연산자를 활용하여 리스트안에 항목이 있는지 확인
print(heroes)

for hero in heroes:#리스트의 모든 항목을 한번씩 방문
    print(hero)
