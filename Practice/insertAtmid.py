class node:
    def __init__(self,value):
        self.prev = None
        self.next = None
        self.data = value

class doubleList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtBeginning(self,value):
        newnode = node(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
    def printing(self):
        curr = self.head
        while(curr!=None):
            print(curr.data,"->",end="")
            curr= curr.next
        print()
        print(self.head.data)
        print(self.tail.data)
        
l = doubleList()
l.insertAtBeginning(4)
l.insertAtBeginning(3)
l.insertAtBeginning(2)
l.insertAtBeginning(1)
l.printing()