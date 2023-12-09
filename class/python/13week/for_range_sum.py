
#!!Notice!! =? 10까지의 합을 구하는 것이다.
sum = 0
for n in range(11):
    print(n, end = " ")
    sum += n
print("The sum = " + str(sum))#0 1 2 3 4 5 6 7 8 9 10 The sum = 55

sum = 0

for n in range(1,11,2): #+2만큼의 숫자 들의 합 
    print(n, end = " ")
    sum += n
print("The sum = " + str(sum))#1 3 5 7 9 The sum = 25

