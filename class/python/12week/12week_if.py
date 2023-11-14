avg = int(input("평균 입력 >> "))
year = int(input("학년 입력 >> "))

if avg >= 70 :
    if year <= 2 :
        print("Pass")
    elif avg >= 80 :
        print("Pass")
    else :
         print("Fail")

else :
    print("Fail")
