class HouseKim:
    lastname = "김";
    def __init__(self,name): #기본적인 생성 즉, 충족되어야하는
            self.fullname = self.lastname + name; #-> 생성이 된 것.
    def travel(self, where):
        print("%s, %s 여행을 가다." %(self.fullname, where));
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" %(self.fullname, other.fullname));
    def fight(self, other):
        print("%s, %s싸우네" % (self.fullname, other.fullname));
    def __add__(self, other):
        print("%s, %s결혼했네" % (self.fullname, other.fullname));
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname));

class Housepark(HouseKim): #왜 클래스의 매개변수로 HouseKim을 사용했는가. -> Kim클래스를 상속 받은 것이다.
    lastname = "박"
    def travel(self, where, day): # 오버라이딩 kim클래스에도 존재하는 travel을 오버라이딩했다.
        print("%s, %s 여행 %d일 가네." %(self.fullname, where, day));

kim = HouseKim("동우");
park = Housepark("명수");
travel = park.travel("부산", 3);
#print(kim.fight(kim));
print(travel);
