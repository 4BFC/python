# VPS_range = [input().split()]
stack = ['(', ')']
# print(stack[0])
for _ in range(len(stack)):
    if stack[0] == ')':
        print("False")
        break
    if stack[0] == '(':
        if stack[_] == ')':
            print("True")

# print(VPS_range[_])
