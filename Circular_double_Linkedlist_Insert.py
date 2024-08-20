class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            new_node.prev = self.tail
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

    def insert_after(self, prev_node, data):
        if prev_node is None:
            print("The given previous node cannot be null")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
        if prev_node == self.tail:
            self.tail = new_node

    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    def display_backward(self):
        if self.tail is None:
            print("List is empty")
            return
        current = self.tail
        while True:
            print(current.data, end=" ")
            current = current.prev
            if current == self.tail:
                break
        print()

# Example usage:
if __name__ == "__main__":
    cdll = CircularDoublyLinkedList()
    cdll.insert_at_beginning(10)
    cdll.insert_at_beginning(20)
    cdll.insert_at_end(30)
    cdll.insert_after(cdll.head.next, 25)

    print("Circular Doubly Linked List (Forward):")
    cdll.display_forward()

    print("Circular Doubly Linked List (Backward):")
    cdll.display_backward()
