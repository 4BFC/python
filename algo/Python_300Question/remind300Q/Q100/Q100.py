#001
print("Hello World");
#011
import string

samsung = 50000;
my_samsung = 10;

total = samsung * my_samsung
print(total);

#013
# >> s = "hello" 
# >> t = "python" 
# 두 변수를 이용하여 아래와 같이 출력해보세요. 
# 실행 예: 
# hello! python
s = "hello";
t = "python";
print(s +'! ' +t);

# 015 type 함수
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
# >> a = "132"
a = "132"
print(type(a))

# 016 문자열을 정수로 변환 문자열 '720'를 정수형으로 변환해보세요.
# >> num_str = "720"
num_str = "720"
# num_str = 720;
# print(type(num_str))
num_str = int(num_str)
print(type(num_str))


# ***017 정수를 문자열 100으로 변환 정수 100을 문자열 '100'으로 변환해보세요.
# num = 100
print(type('100'))
#->
num = 100
num = str(num)
print(type(num))

# 018 문자열을 실수로 변환 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
num1 = "15.79"
num1 = float(num1)
print(type(num1))

# 019 문자열을 정수로 변환 year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = '2023'
year = int(year)
print(year -3)
print(year -2)
print(year -1)

# 020 파이썬 계산 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 
#총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

item = 48584;
month = 36;
price = item*month;
print(price);

#17