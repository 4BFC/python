my_name = "김동우"
your_name = "김왼손의 왼손코딩"
print("*Slicing : 썰다_슬라이스 _ 떼어내기,\n",
my_name[1:2],"\n",
my_name[2:3],"\n",
your_name[5:7],"\n",
your_name[4:],"\n",
)

fruit_str = '거봉 수박 포도 복숭아 망고 딸기 배 참외 찹쌀떡'
print("*split : (method) 문자열을 공백 단위로 자른다.\n",
my_name.split(),"\n",
your_name.split(),"\n",
fruit_str.split(),"\n",
)

print("*Docstring : 큰따옴표 세개를 사용 = 주석을 사용하듯이 사용\n",
)
#end=는 뭐지?
print("\'', end='\'\n",
'집단지성', end= '&\t'
);print("여러개의 명령")

my_List = [1,2,3]
std = ['이에스', '이에스2', '이에스3']
std.append('토미')
std.append('찹쌀떡')
animals = []
animals.append('코알라')
animals.append("하이에나")
animals.append('바다소')
animals.append('땅다람쥐')
print("List : Array와 비슷하게 생김 : immutable : 값변경 불가능, mutable : 값은 변경 가능\n",
my_List, type(my_List),"\n",
std, type(std),"\n",
animals
)

My_Rul = "1 2 3 4 5"
cycle = My_Rul.split()
print(cycle[0], cycle[1])

# my_rul = "1, 2, 3, 4"
# coma = ','
# my_rul.split(coma)
# print(my_rul.split(coma))

del animals[1]
print("Index : 주소, element : 내용물\n",
"하이에나가 사라짐 ", animals,"\n",)
#animals[3],"\n") 
animals.append("강아지")
animals.append("바다사자")
print("Slicing : 잘라내는 것\n",
animals,"\n",
animals[0:2],"\n",
"Slicing은 chunk를 기준으로 나뉜다.\n std = [A,B,C,D]에 std[0:1]이면 'A'만 출력된다."
)
#GANADA = ['나, 기, 오, 카, 케, 츠, 티, 파, 타, 리, 우, 갸, 이, 하, 수, 차']
print("list.sort() : 가나다 순을 정렬\n",
animals.sort(), animals,"\n",
"list.count() : 리스트의 수량을 알 수 있음\n",
animals.count("하이에나"),"\n",
animals.count('코알라'),"\n",
"len(array/list) : 내장 함수 =>\n",
len(animals))
print("외장/내장 함수 참고자료 :\n https://wayhome25.github.io/python/2017/02/23/py-function-method-list/")

print("Indexing : element(Indexing) : 123(0), 'abc'(1), True(2)");
animals.append('바다코끼리');
animals.append('스컹크');
animals.append('아나콘다');
print(animals);

print("이렇게 배열을 통해서 불러오는 것이 .'Indexing'이다. \t:", animals[3]+"\n"); 

del animals[4];

print(animals);

animals.append('코알라');
animals.append('냥고양이');
print(animals);

print("\n슬라이스/slicing 방법은 띄어쓰기/chunk를 기준(앞에 시작이 0이다.으로 한다.");
print(animals[1:3]);

#23강

print("sort하기 이전 : ", animals);
animals.sort();
print("sort한 후 : ", animals);

animals.append('바다소');
print("list.count() : 어떠한 요소, 값이 리스트에 몇개나 있나")
print(animals.count('바다소'));
print(len(animals)); #len() 함수는 리스트 전체의 값을 알려준다.

#24

print("Tuple : list처럼 값을 모으는 것 하지만 Tuple은 값을 변경할 수 없음");
my_tuple = ();
print(my_tuple);
print(type(my_tuple));

my_tuple = 1,2,3; #my_tuple = (1,2,3); -> 괄호를 사용해도 괜찮다.
print(my_tuple);

#25
print("Packing : 여러개 값을 하나로 묶는 것/Unpacking : 묶여있는 값을 여러개로 푸는 것");
my_tuple = 1,2,3; #-> packing

num1, num2, num3 = my_tuple; # -> unpacking
print(num1,num2,num3);
num1, num2 = num2, num1; #num2, num1이 하나의 패킹이 되고 왼쪽으로 언패킹이된 것.
print(num1,num2,num3);