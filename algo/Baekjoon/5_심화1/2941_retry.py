Alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
N = "nljj"  # 1개 2개
cnt = []
# 큰거에서 부터 작은걸로
for ii in range(len(Alp)):  # ii -> Alp
    # print(f"{i} : ")
    for i in N:  # N -> i
        # if Alp[ii] in N:
        if Alp[ii] in N:
            print(ii)

            # cnt.append(ii)
            # print(f"in is => {ii}")
            # print(f"ii => {ii}")
            # cnt.append(N.count(ii))
            # cnt += 1
        # elif ii not in N:
        #     print(N[i])
        # else:
        #     print(i)
        # else:
        #     print("None")
        # print(N.count(i))
        # print(N.count(ii))

# print(cnt)
# print(set(cnt))
# print(sum(set(cnt)))
