result = input()

if 100 == int(result) or int(result) >= 90:
    print('A')
elif 89 == int(result) or int(result) >= 80:
    print('B')
elif 79 == int(result) or int(result) >= 70:
    print('C')
elif 69 == int(result) or int(result) >= 60:
    print('D')
else:
    print('F')
