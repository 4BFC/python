N = int(input())
score = []
result = 0
for _ in range(N):
    score.append(int(input()))
    M = max(score)
for _ in range(N):
    result += (score[_]/M*100)
print(result/N)
