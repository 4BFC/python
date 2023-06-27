#mod2.py
PI = 3.141592;
class Math: #반지를 구하는 클래스
    def solv(self, r):
        return PI *(r**2);   # r**는 r^2을 의미한다.
def sum(a,b):
        return a+b;

if __name__ == "__main__": #__name__이 메인(main). 즉, 컴파일 화면이 메인일 때만 아래의 프린트 등들이 실행 된다.
    print(PI);
    a = Math();
    print(a.solv(2));
    print(sum(PI, 4.4));