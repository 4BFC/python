class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_push(self, item):
        self.stack.append(item)

    def is_pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)


stack = Stack()

stack.is_push(10)
stack.is_push(20)
stack.is_push(30)

# 현재 stack의 모습
# 30
# 20
# 10

print(stack.is_pop())  # 30 -pop
print(stack.peek())  # 20 - peek
print(stack.size())  # 2
print(stack.is_empty())  # False
