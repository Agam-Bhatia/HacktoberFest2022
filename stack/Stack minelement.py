from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
        self.auxContainer = deque()
        self.min = None

    def push(self, val):
        if self.is_empty() or val <= self.min:
            self.container.append(val)
            self.auxContainer.append(val)
            self.min = val

        else:
            self.container.append(val)


    def pop(self):
        if self.container.pop() == self.min:
            self.container.pop()
            self.auxContainer.pop()
        else:
            self.container.pop()

    def peek(self):
        return self.container[-1]

    def size(self):
        return len(self.container)

    def is_empty(self):
        return len(self.container) == 0

    def minimum(self):
        return self.auxContainer[-1]

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(-22)
    s.push(4)
    s.push(8)
    s.push(-1)

    print(s.minimum())

