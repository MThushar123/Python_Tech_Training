class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue
        self.size = 0     # Tracks the number of elements

    def is_empty(self):
        return self.size == 0

    def enqueue(self, data):
        """Add an element to the rear of the queue."""
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Remove and return the element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If queue becomes empty
            self.rear = None
        self.size -= 1
        return data

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.front.data

    def get_size(self):
        """Return the current size of the queue."""
        return self.size

    def display(self):
        """Print the queue elements from front to rear."""
        if self.is_empty():
            print("Queue is empty")
            return
        current = self.front
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Queue (front to rear):", " -> ".join(elements))

# Example usage with output
if __name__ == "__main__":
    # Create a queue
    q = Queue()

    # Enqueue elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()  # Output: Queue (front to rear): 10 -> 20 -> 30

    # Peek front
    print("Front element:", q.peek())  # Output: Front element: 10

    # Dequeue
    print("Dequeued:", q.dequeue())  # Output: Dequeued: 10
    q.display()  # Output: Queue (front to rear): 20 -> 30

    # Check size
    print("Size:", q.get_size())  # Output: Size: 2

    # Dequeue until empty
    print("Dequeued:", q.dequeue())  # Output: Dequeued: 20
    print("Dequeued:", q.dequeue())  # Output: Dequeued: 30
    print("Is empty:", q.is_empty())  # Output: Is empty: True
