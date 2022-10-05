class BST1:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeOperation1:
    def __init__(self, val):
        self.root = BST1(val)

    def insert(self, key):
        return self.inserting(self.root, key)


    def inserting(self, root, key):
        if root is None:
            return BST1(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.inserting(root.right, key)
            else:
                root.left = self.inserting(root.left, key)

        return root

    def inorder(self):
        if self.root:
            self.inorder(self.root.left)
            print(str(self.root.val) + " - ", end =" ")
            self.inorder(self.root.right)


if __name__ == "__main":
    tree = TreeOperation1(50)
    tree.insert(30)
    # tree.insert(tree, 20)
    # tree.insert(tree, 40)
    # tree.insert(tree, 70)
    # tree.insert(tree, 60)
    # tree.insert(tree, 80)

    tree.inorder(tree)

