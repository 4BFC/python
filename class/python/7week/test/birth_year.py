data = ['쥐','소','범','토끼','용','뱀','말','양','원숭이','닭','개','돼지']

birthYear = int(input("when is your birthyear? : "))
year = (birthYear + 8) % 12
print(data[year])
