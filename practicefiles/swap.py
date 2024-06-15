# swap

a = 3
b = 5
print("before")
print(f"a의 값은 {a}입니다.")
print(f"b의 값은 {b}입니다.")

a, b = b, a
print("after")
print(f"a의 값은 {a}입니다.")
print(f"b의 값은 {b}입니다.")


a = 3
b = 5
print("before")
print(f"a의 값은 {a}입니다.")
print(f"b의 값은 {b}입니다.")

temp = a
a = b
b = temp

print("after")
print(f"a의 값은 {a}입니다.")
print(f"b의 값은 {b}입니다.")
