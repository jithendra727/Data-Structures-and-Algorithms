from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue.popleft()
            print(f"Dequeued: {removed_item}")
            return removed_item
        else:
            print("Queue is empty. Cannot dequeue.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty.")
            return None

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", list(self.queue))


# Example usage
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    
    q.display()
    
    q.dequeue()
    q.display()

    print(f"Front element: {q.peek()}")
    print(f"Queue size: {q.size()}")
