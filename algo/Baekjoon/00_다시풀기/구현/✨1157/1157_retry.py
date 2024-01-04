N = list(input().upper())
# N.upper()
apl = list(set(N))
cnt = []
print(apl)
for i in apl:
    cnt.append(N.count(i))
# print(cnt)
# print(cnt.count(max((cnt))))
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(apl[cnt.index(max(cnt))])
