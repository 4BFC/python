# 파이썬의 입출력

* 함수 안에서 선언한 변수의 효력 범위
```
a = 1

def vartest(a):
    a = a + 1
    return a

print(vartest(a))
print(a)

```
> 함수의 효력 범위를 잘 이해하고 지역(local)과 전역(global)의 범위를 생각하며 get과 set의 구조를 짤 때 get과 set의 위치를 유의해서 짜야한다.