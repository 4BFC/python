import sys


class Stack:
    def __init__(self) -> None:
        self.stack = []  # => 생성자

    def pushX(self, item):
        return self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if not len(self.stack) == 0:
            return 0
        else:
            return -1

    def top(self):
        if not self.empty():
            return self.stack[-1]
        else:
            return -1


N = int(sys.stdin.readline())
stack = Stack()
for _ in range(N):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "push":
        stack.pushX(cmd[1])
    if cmd[0] == "pop":
        print(stack.pop())
    if cmd[0] == "top":  # peek
        print(stack.top())
    if cmd[0] == "size":
        print(stack.size())
    if cmd[0] == "empty":
        print(stack.empty())
else:
    print("wrong input")
