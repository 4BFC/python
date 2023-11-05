#딕셔너리
items = {'커피':7,'볼팬':3,'라면':5,'우유':1,'콜라':4,'껌':10}
#입력하기 
inputitme = input('입력하시오. ')
#결과
result = items.get(inputitme)
print(result,'개') 
