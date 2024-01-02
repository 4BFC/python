# N = input()  # 'ObjectOrientedProgramming1 3.0 A+'
num = []
grade = []

for i in range(20):
    N = input()
    lst = N.split(' ')
    if lst[2] != 'P':
        num.append(float(lst[1]))
        if lst[2] == 'A+':
            grade.append(4.5)
        elif lst[2] == 'A0':
            grade.append(4.0)
        elif lst[2] == 'B+':
            grade.append(3.5)
        elif lst[2] == 'B0':
            grade.append(3.0)
        elif lst[2] == 'C+':
            grade.append(2.5)
        elif lst[2] == 'C0':
            grade.append(2.0)
        elif lst[2] == 'D+':
            grade.append(1.5)
        elif lst[2] == 'D0':
            grade.append(1.0)
        elif lst[2] == 'F':
            grade.append(0.0)
sum_n = []
for i in range(len(num)):
    n = float(grade[i]) * float(num[i])
    sum_n.append(n)


print(num)
print(grade)
print(round(sum(sum_n)/sum(num), 6))
# print(type(float(num[0])))
print(len(num))
print(len(grade))

# num = int(lst[1])
# print(num)
# print(int(lst[1]) * 4.5)
