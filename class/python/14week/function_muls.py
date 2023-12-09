def threeMultiple(n):
    if(n % 3 == 0) :
        return True #boolen으로 값을 반환 
    else:
        return False

#three = threeMultiple(4)
#print(three)

def threeMuls2(num):
    for n in range(1,num) :
        if threeMultiple(n): #3의 배수만 처리하는 함수를 이용해 if문 처리 
            print(n, end = ' ')
    print()
threeMuls2(31)
