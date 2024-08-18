class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_node(self.root, data)

    def _insert_node(self, root, data):
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert_node(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert_node(root.right, data)

    def in_order_traversal(self):
        print("In-order Traversal:", end=" ")
        self._in_order_traversal(self.root)
        print()

    def _in_order_traversal(self, root):
        if root:
            self._in_order_traversal(root.left)
            print(root.data, end=" ")
            self._in_order_traversal(root.right)

    def pre_order_traversal(self):
        print("Pre-order Traversal:", end=" ")
        self._pre_order_traversal(self.root)
        print()

    def _pre_order_traversal(self, root):
        if root:
            print(root.data, end=" ")
            self._pre_order_traversal(root.left)
            self._pre_order_traversal(root.right)

    def post_order_traversal(self):
        print("Post-order Traversal:", end=" ")
        self._post_order_traversal(self.root)
        print()

    def _post_order_traversal(self, root):
        if root:
            self._post_order_traversal(root.left)
            self._post_order_traversal(root.right)
            print(root.data, end=" ")

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()

    # Insert nodes into the binary tree
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    # Print traversals
    tree.in_order_traversal()   # Output: 20 30 40 50 60 70 80
    tree.pre_order_traversal()  # Output: 50 30 20 40 70 60 80
    tree.post_order_traversal() # Output: 20 40 30 60 80 70 50
