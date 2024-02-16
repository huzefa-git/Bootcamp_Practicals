class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.data = value

class Tree:
    def __init__(self):
        self.root = None

    def insertion(self, value):
        newnode = Node(value)
        if self.root is None:
            self.root = newnode
        else:
            curr = self.root
            while True:
                if value < curr.data:
                    if curr.left is None:
                        curr.left = newnode
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = newnode
                        break
                    else:
                        curr = curr.right

    def height(self):
        s = self.helpheight(self.root)
        print(s - 1)

    def helpheight(self, root):
        if root is None:
            return 0
        else:
            leftnode = self.helpheight(root.left)
            rightnode = self.helpheight(root.right)
            return max(leftnode, rightnode) + 1

    def delete(self, key):
        self.root = self.helpdelete(self.root, key)

    def helpdelete(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self.helpdelete(root.left, key)
        elif key > root.data:
            root.right = self.helpdelete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.data = curr.data
                root.right = self.helpdelete(root.right, curr.data)
        return root

t = Tree()
t.insertion(5)
t.insertion(4)
t.insertion(3)
t.insertion(2)
t.delete(5)
t.height()