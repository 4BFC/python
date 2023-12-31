N = ['but', 'i', 'wont', 'hesitate', 'no', 'more',
     'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
s = []
n = []
l = 0
for i in N:
    s.append(len(i))
    # if l <= len(i):
    #     print(i)
    #     l = len(i)
    # s.append(i)
s.sort()
print(s)

for i in range(len(s)):
    # print(f"{s[i]} : {N[i]}")
    for ii in N:
        if s[i] == len(ii):
            # print(f"{s[i]} : {len(ii)}")
            n.append(ii)
print(set(n))

# if s[i] == len(N[i]):
#     n.append(N[i])
