class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def insertAtBeg(self,data):
        newnode= node(data)
        if self.head ==None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def printing(self):
        curr = self.head
        while(curr!=None):
            print(curr.data,"->",end="")
            curr = curr.next
        print("none")

l = sll()
l.insertAtBeg(3)
l.insertAtBeg(2)
l.insertAtBeg(1)
l.printing()