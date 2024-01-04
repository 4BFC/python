croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# N_len = 0
N = input()

for i in croa:
    if i in N:
        N = N.replace(i, '*')
        # N_len = len(N)
# print(N_len)
print(len(N))
