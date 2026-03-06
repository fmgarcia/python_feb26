class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)  # Output: [1, 2, 3]
    print(queue.dequeue())  # Output: 1
    print(queue.peek())  # Output: 2
    print(queue.size())  # Output: 2