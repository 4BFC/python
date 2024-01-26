# input이 아닌 sys로 문제 다시 풀어볼 것.
# 공백때문에 문제가 된다. 그래서 split을 무조건 사용
# 실행이 되어도 문제라는 것이다.
# 공백이 있는지 확인하는 방법도 찾아 봐야한다.
import sys
stack = []
# n = sys.stdin.readlines()
n = int(sys.stdin.readline())

for i in range(n):
    cmd = sys.stdin.readline()

    if len(cmd) > 2:  # 이게 왜되는건지 확인
        stack.append(int(cmd[2]))
        # print(stack)
    # if cmd == '1':
    #     stack.append(cmd[2])
    elif cmd[0] == '2':
        if len(stack) != 0:
            print(stack.pop())
        elif len(stack) == 0:
            print(-1)
    elif cmd[0] == '3':
        print(len(stack))
    elif cmd[0] == '4':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == '5':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
