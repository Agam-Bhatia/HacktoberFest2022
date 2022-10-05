

class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right= None


class BinaryTree():
    def __init__(self, val):
        self.root = Node(val)

    def print_tree(self):
        return self.InorderTraversal(tree.root, traversal = "")




    def InorderTraversal(self, start  , traversal=""):
        if start:
            traversal = self.InorderTraversal(start.left, traversal)
            traversal += (str(start.val) + " - ")
            traversal = self.InorderTraversal(start.right, traversal)

        return traversal

    def delDeepest(self, root, delNode):
        q = []
        q.append(tree.root)
        while(len(q)):
            temp = q.pop(0)
            if temp.val is delNode:
                delNode = None
                return

            if temp.right:
                if temp.right is delNode:
                    temp.right = None
                    return
                else:
                    q.append(temp.right)

            if temp.left:
                if temp.left is delNode:
                    temp.left = None
                    return
                else:
                    q.append(temp.left)






    def NodeDeletion(self, NodeToDelete):
        if self.root == None:
            return "Empty"
        if self.root.val == NodeToDelete:
            if self.root.left == None and self.root.right == None:
                self.root = None
                return None
            else:
                return self.root

        q = []
        q.append(self.root)
        temp = None
        keyNode = None
        while (len(q)):
            temp = q.pop(0)
            if temp.val is NodeToDelete:
                keyNode = temp

            if temp.left :
                q.append(temp.left)

            if temp.right:
                q.append(temp.right)

        if keyNode:
            x = temp.val
            self.delDeepest(self.root, temp)
            keyNode.val = x

        return self.root

if __name__ == "__main__":
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

    print(tree.print_tree())
    tree.NodeDeletion(2)
    print(tree.print_tree())



