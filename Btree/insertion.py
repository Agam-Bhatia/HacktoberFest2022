class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, value):
        self.root = Node(value)

    def print_tree(self, t_type):
        if t_type =="preorder":
            print("Pre-order traveral")
            return self.preorder_traversal(tree.root, "")
        elif t_type =="postorder":
            print("Post-order traveral")
            return self.postorder_traversal(tree.root, "")
        elif t_type == "inorder":
            print("In-order traveral")
            return self.inorder_traversal(tree.root, "")



    def preorder_traversal(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_traversal(start.left, traversal )
            traversal = self.preorder_traversal(start.right, traversal )
        return traversal

    def postorder_traversal(self, start, traversal):
        if start:
            traversal = self.postorder_traversal(start.left, traversal)
            traversal = self.postorder_traversal(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def inorder_traversal(self, start, traversal):
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_traversal(start.right, traversal)

        return traversal


tree = BinaryTree(1)
#           1
tree.root.left = Node(2)
#            1
#          /
#         2

tree.root.right = Node(3)
#            1
#          /   \
#         2     3
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
#            1
#          /   \
#         2     3
#       / \
#      4   5
tree.root.right.right = Node(7)
tree.root.right.left = Node(6)
#            1
#          /   \
#         2      3
#       /  \   /   \
#      4    5  6    7

print(tree.print_tree("preorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("inorder"))

