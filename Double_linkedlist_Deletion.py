class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedListDeletion:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Method to delete node from the beginning of the doubly linked list
    def delete_from_beginning(self):
        if self.is_empty():
            print("Doubly linked list is empty. Deletion not possible.")
            return
        if self.head == self.tail:  # Only one element in the list
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            if self.head:  # Check if the list isn't empty after deletion
                self.head.prev = None
        self.size -= 1

    # Method to delete node from the end of the doubly linked list
    def delete_from_end(self):
        if self.is_empty():
            print("Doubly linked list is empty. Deletion not possible.")
            return
        if self.head == self.tail:  # Only one element in the list
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            if self.tail:  # Check if the list isn't empty after deletion
                self.tail.next = None
        self.size -= 1

    # Method to delete node at a specific index in the doubly linked list
    def delete_at(self, index):
        if self.is_empty():
            print("Doubly linked list is empty. Deletion not possible.")
            return
        if index < 0 or index >= self.size:
            raise IndexError(f"Index: {index}, Size: {self.size}")
        if index == 0:
            self.delete_from_beginning()
        elif index == self.size - 1:
            self.delete_from_end()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1

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

    # Method to insert data at the end of the doubly linked list (used for demonstration)
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

if __name__ == "__main__":
    dll = DoubleLinkedListDeletion()

    # Inserting elements for demonstration
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_end(30)
    dll.insert_at_end(40)
    dll.insert_at_end(50)
    dll.display()  # Output: Doubly linked list: 10 20 30 40 50

    # Deleting element from the beginning
    dll.delete_from_beginning()
    dll.display()  # Output: Doubly linked list: 20 30 40 50

    # Deleting element from the end
    dll.delete_from_end()
    dll.display()  # Output: Doubly linked list: 20 30 40

    # Deleting element at specific index
    dll.delete_at(1)  # Deleting element at index 1
    dll.display()  # Output: Doubly linked list: 20 40
