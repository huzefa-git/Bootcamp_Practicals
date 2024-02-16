class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.right.right = node(5)
print("inorder:")
inorder(root)
print()
print("postorder:")
postorder(root)
print()
print("preorder:")
preorder(root)
