class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty, no node to delete.")
            return
        if self.head.next == self.head:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head

    def delete_from_end(self):
        if self.tail is None:
            print("List is empty, no node to delete.")
            return
        if self.tail.prev == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail

    def delete_node(self, del_node):
        if self.head is None or del_node is None:
            print("List is empty or node to delete is null.")
            return

        if self.head == del_node:
            self.delete_from_beginning()
            return

        if self.tail == del_node:
            self.delete_from_end()
            return

        del_node.prev.next = del_node.next
        del_node.next.prev = del_node.prev

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
    cdll.insert_at_end(10)
    cdll.insert_at_end(20)
    cdll.insert_at_end(30)
    cdll.insert_at_end(40)

    print("Circular Doubly Linked List (Forward):")
    cdll.display_forward()

    cdll.delete_from_beginning()
    print("List after deleting from beginning:")
    cdll.display_forward()

    cdll.delete_from_end()
    print("List after deleting from end:")
    cdll.display_forward()

    cdll.delete_node(cdll.head.next)
    print("List after deleting specific node:")
    cdll.display_forward()
