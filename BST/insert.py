class BST:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def insert(root, key):
    if root is None:
        return BST(key)

    else:
        if root.val == key:
            return root
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + " - ", end=" ")
        inorder(root.right)

#
if __name__ == "__main__":
    tree = BST(50)

    tree = insert(tree, 30)
    tree = insert(tree, 20)
    tree = insert(tree, 40)
    tree = insert(tree, 70)
    tree = insert(tree, 60)
    tree = insert(tree, 80)
    inorder(tree)
#     # print(tree.insert(tree, ""))
#
#
#
#
#
#
