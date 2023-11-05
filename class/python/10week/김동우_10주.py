#편의점 재고 dic 변수 선언 
items = {'커피':7,'볼팬':3,'라면':5,'우유':1,'콜라':4,'껌':10}

#keys()함수를 통한 를 이용한 현재 편의점 재고 콘솔에서 보여주기
print('현재 편의점에서 가지고 있는 물품 내역입니다.\n',list(items.keys()))
print()

#재고 입력받기()
stuff_key = input('재고를 확인 할 물건을 입력하세요. ==> ')
print()

#dic의 value를 확인할 수 있는 방법은 여러가지 이지만 본인은 get을 이용한 방법을 선택했다.
result = items.get(stuff_key)
print(f'입력하신 \'{stuff_key}\'의 현재 재고는 {result}개 입니다.') 
