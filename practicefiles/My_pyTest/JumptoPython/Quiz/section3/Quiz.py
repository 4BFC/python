#js에서도 적용해보면 같다.
#구조를 짤 때 get과 set을 더욱 중시 해서 적용해야한다.
a = 1


def vartest(a):
    a = a + 1
    return a


print(vartest(a))
print(a)
