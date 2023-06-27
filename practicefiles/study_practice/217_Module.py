import imp
import mod1 #모듈을 불러오는, 임포틑 시키는 방법
from mod2 import sum #모듈에서 내가 원하는 함수만 사용하는 방법
import mod2
print(sum(1,2));
print(mod1.sum(3,4));
print(mod2.PI);
a = mod2.Math();
print(a.solv(2));