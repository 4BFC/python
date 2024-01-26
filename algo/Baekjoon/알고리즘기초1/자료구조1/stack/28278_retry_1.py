import sys
n = sys.stdin.readline()
stack = []
for i in range(int(n)):
    cmd = sys.stdin.readline().split()
    if cmd[0] == '1':
        stack.append(int(cmd[1]))
    if cmd[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    if cmd[0] == '3':
        print(len(stack))
    if cmd[0] == '4':
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    if cmd[0] == '5':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
