N = []
for _ in range(28):
    N.append(input())
exc = []

for i in range(1, 31):  # 학생 수 30
    # for ii in range(len(N)):  # 제출 학생 28
    if str(i) not in N:
        exc.append(i)
        print(i, end=" ")
    print()
print(exc)
# lst = list(set(exc))

# lst.sort()
for i in range(len(exc)):
    print(exc[i])
# print(set(exc))


# students = [i for i in range(1,31)]

# for _ in range(28):
#     applied = int(input())
#     students.remove(applied) #소거

# print(min(students))
# print(max(students))
