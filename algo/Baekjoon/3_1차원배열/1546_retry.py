N = int(input())
score = list(map(int, input().split()))
result = 0
M = max(score)
# for _ in range(N):
#     score.append(int(input()))
    
for _ in range(N):
    result += (score[_]/M*100)
print(result/N)
