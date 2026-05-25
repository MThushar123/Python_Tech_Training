class Queue_Using_Stacks:
    def __init__(self):
        self.stack1 = [] 
        self.stack2 = []
    
    def enqueue(self, item):
        self.stack1.append(item)
        print(f"Enqueued: {item}")
    
    def dequeue(self):

queue = Queue_Using_Stacks()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
