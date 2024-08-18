from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class CompleteBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return

        # Use a queue to perform level-order traversal
        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = new_node
                break
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                break
            else:
                queue.append(current.right)

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

    def is_complete_binary_tree(self):
        if self.root is None:
            return True

        # Use a queue for level-order traversal
        queue = deque([self.root])
        flag = False

        while queue:
            current = queue.popleft()

            if current.left:
                if flag:
                    return False
                queue.append(current.left)
            else:
                flag = True

            if current.right:
                if flag:
                    return False
                queue.append(current.right)
            else:
                flag = True

        return True

# Example usage:
if __name__ == "__main__":
    tree = CompleteBinaryTree()

    # Insert nodes into the complete binary tree
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)

    # Print traversals
    tree.in_order_traversal()   # Output: 4 2 5 1 6 3
    tree.pre_order_traversal()  # Output: 1 2 4 5 3 6
    tree.post_order_traversal() # Output: 4 5 2 6 3 1

    # Check if the tree is complete
    if tree.is_complete_binary_tree():
        print("The tree is a complete binary tree.")
    else:
        print("The tree is not a complete binary tree.")
