class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Could raise an exception, but returning None for simplicity

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

# Sample usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Stack after pushing elements:")
    stack.display()
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack after popping:")
    stack.display()
