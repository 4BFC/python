a =[3,6,9,12,15,18,21,27]
print(a[:3])
print(a[3:])
print(a[:]) #all

b = "my name"
print(b[1])

#add
b = [3,6,9,13,15,18,21,27]
b[3] = 12
print(b)

#insert
a = [3,5,7,9]
a.insert(0,1)
print(a)
a.insert(2,4)
print(a)

#append
future = []
future.append("AI")
future.append("빅데이터")
future.append("자율주행")
future.append("사물인터넷")

print("미리 기술 핵심분야")

#sep역할
print(future, sep=",") #['AI', '빅데이터', '자율주행', '사물인터넷']

#sort
#future.sort()
print(future, sep=",") #['AI', '빅데이터', '사물인터넷', '자율주행']

#reverse : 순서의 역으로
#future.reverse()
print(future, sep=",") #['사물인터넷', '자율주행', '빅데이터', 'AI']

#sort(reverse = True) : 리스트 값을 내림차수능로 변경
future.sort(reverse=True)
print(future, sep=",") #['자율주행', '사물인터넷', '빅데이터', 'AI']
