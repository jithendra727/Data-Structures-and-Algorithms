class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class FullBinaryTree:
    def __init__(self):
        self.root = None

    def create_full_binary_tree(self, elements):
        if not elements:
            return
        self.root = self._create_full_binary_tree(elements, 0)

    def _create_full_binary_tree(self, elements, index):
        if index >= len(elements):
            return None

        node = Node(elements[index])

        # Full binary tree property: Each node has 0 or 2 children
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(elements) and right_index < len(elements):
            node.left = self._create_full_binary_tree(elements, left_index)
            node.right = self._create_full_binary_tree(elements, right_index)

        return node

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

    def is_full_binary_tree(self):
        return self._is_full_binary_tree(self.root)

    def _is_full_binary_tree(self, node):
        if node is None:
            return True  # An empty tree is considered full

        # If leaf node, return True
        if node.left is None and node.right is None:
            return True

        # If both children are present
        if node.left is not None and node.right is not None:
            return self._is_full_binary_tree(node.left) and self._is_full_binary_tree(node.right)

        # If one child is missing
        return False

if __name__ == "__main__":
    tree = FullBinaryTree()

    # Example array to create a full binary tree
    elements = [1, 2, 3, 4, 5, 6, 7]
    tree.create_full_binary_tree(elements)

    # Print traversals
    tree.in_order_traversal()
    tree.pre_order_traversal()
    tree.post_order_traversal()

    # Check if the tree is full
    if tree.is_full_binary_tree():
        print("The tree is a full binary tree.")
    else:
        print("The tree is not a full binary tree.")
