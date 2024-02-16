from typing import Any


class node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value
class trees:
    def __init__(self):
        self.root = None
    
    def insertion(self,value):
        newnode = node(value)
        if self.root==None:
            self.root = newnode
        else:
            curr = self.root
            while True:
                if value < curr.data:
                    if curr.left == None:
                        curr.left = newnode
                        break

                    else:
                        curr = curr.left

                else:
                    if curr.right == None:
                        curr.right = newnode
                        break
                    else:
                        curr = curr.right

def helpsearch(root,key):
    if root==None or root.data ==key:
        return root
    elif key<root.data:
        return helpsearch(root.left,key)
    else:
        return helpsearch(root.right,key)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def count(root):
    if root == None:
        return 0
    if root:
        leftnode=count(root.left)
        rightnode=count(root.right)
        return leftnode+rightnode+1

r = trees()
r.insertion(5)
r.insertion(3)
r.insertion(7)
r.insertion(1)
r.insertion(9)
inorder(r.root)
s=helpsearch(r.root,8)
if s==None:
    print("not found")
else:
    print("found")
print(count(r.root))