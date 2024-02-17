N,M = 5,3   
num = [1, 2, 3, 1, 2]
NUM = [0] * (len(num)+1)
for i in range(len(num)):
    NUM[i+1] = NUM[i] + num[i]
    if (i+1) % 3 == 0:
        print(i)
        idx = NUM.index(i+1)
        print(NUM[idx])
print(NUM)

