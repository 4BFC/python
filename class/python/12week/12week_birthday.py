while "True" :
    #연도 입력받기
    birth_year = int(input("태어난 연도를 입력하세요. ->"))

    line = birth_year % 12


    #12로 나눈 나머지 값 비교
    if line == 0 : print(f"원숭이 => {birth_year}")
    elif line == 1: print(f"닭 => {birth_year}")
    elif line == 2: print(f"개 => {birth_year}")
    elif line == 3: print(f"돼지 => {birth_year}")
    elif line == 4: print(f"쥐 => {birth_year}")
    elif line == 5: print(f"소 => {birth_year}")
    elif line == 6: print(f"범 => {birth_year}")
    elif line == 7: print(f"토끼 => {birth_year}")
    elif line == 8: print(f"용 => {birth_year}")
    elif line == 9: print(f"뱀 => {birth_year}")
    elif line == 10: print(f"말 => {birth_year}")
    elif line == 11: print(f"양 => {birth_year}")
    else :  print("다시 입력해주세요 => {birth_year}")
