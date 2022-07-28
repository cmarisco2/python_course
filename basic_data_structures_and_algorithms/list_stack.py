# Demo basic Stack functionality with a Python List

class Stack:

    def __init__(self) -> None:
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return len(self._stack) == 0

    def peek(self):
        return self._stack[-1]

    def size(self):
        return len(self._stack)


my_stack = Stack()
print(f'is my_stack empty? {my_stack.is_empty()}')
stuff = ['a', 1, '3.14']
print('pushing 3 items to my stack')
for thing in stuff:
    my_stack.push(thing)
print(f'is my_stack empty? {my_stack.is_empty()}')
print(f'my stack size: {my_stack.size()}')
print(f'the top of my stack is: {my_stack.peek()}')
my_stack.pop()

print(
    f'popping the top element.\nnow the top of my stack is: {my_stack.peek()}')
