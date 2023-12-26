n = ['apple']
# N = input()
N = 'ace'
# N = ['a', 'b', 'c']
for i in range(len(N)):
    # print(n in N[i]) # -> Error
    # -> False : 이유는 n은 list이다. 즉, str로 형변환을 해줘야 한다.
    print(f"f/{N[i]}:{type(N[i])}{type(n)}=>{N[i] in n}")
    print(f"t/{N[i]}:{type(N[i])}{type(str(n))}=>{N[i] in str(n)}")  # -> True
# for i in range(len(n)):
#     for ii in N:
#         print(n[i] in ii)
