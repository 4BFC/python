N = 'Mississipi'  # Mississipi baaa
n = []
for i in N:
    # print(f"{i} = {N.count(i)}")
    n.append(N.count(i))
    # for ii in n:
    #     print(n.index(ii))
#     for ii in n:
#         # print(N[ii])
#         print(n.index(ii), end=" ")

if 1 < len(set(n)):
    print('?')
else:
    print(N[n.index(max(n))])
print(n)
print(n.count(max(n)))
# print(set(n))
# print(n.index(max(n)))
