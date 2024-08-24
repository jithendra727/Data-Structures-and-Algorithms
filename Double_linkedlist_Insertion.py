class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedListInsertion:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Method to insert data at the beginning of the doubly linked list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # Method to insert data at the end of the doubly linked list
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    # Method to insert data at a specific index in the doubly linked list
    def insert_at(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError(f"Index: {index}, Size: {self.size}")
        if index == 0:
            self.insert_at_beginning(data)
        elif index == self.size:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    # Method to check if the doubly linked list is empty
    def is_empty(self):
        return self.size == 0

    # Method to display the elements of the doubly linked list
    def display(self):
        current = self.head
        print("Doubly linked list:", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    dll = DoubleLinkedListInsertion()

    # Inserting elements at the beginning
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(30)
    dll.display()  # Output: Doubly linked list: 30 20 10

    # Inserting elements at the end
    dll.insert_at_end(40)
    dll.insert_at_end(50)
    dll.display()  # Output: Doubly linked list: 30 20 10 40 50

    # Inserting element at specific index
    dll.insert_at(2, 25)  # Inserting 25 at index 2
    dll.display()  # Output: Doubly linked list: 30 20 25 10 40 50
