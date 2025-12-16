#Stack Implementation using Arrays – Implement a stack using an array with push, pop, and display operations.

class Stack:
    def __init__(self):
        self.stack = []  # Using a list as the underlying array
        self.top = -1    # Index of the top element (-1 means empty)

    def push(self, item):
        self.stack.append(item)
        self.top += 1
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        item = self.stack.pop()
        self.top -= 1
        print(f"Popped {item} from the stack.")
        return item

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack (top to bottom):", end=" ")
            for i in range(self.top, -1, -1):
                print(self.stack[i], end=" ")
            print()

    def is_empty(self):
        return self.top == -1

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()  # Output: Stack (top to bottom): 30 20 10
stack.pop()      # Output: Popped 30 from the stack.
stack.display()  # Output: Stack (top to bottom): 20 10
