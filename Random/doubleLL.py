class node:
    def __init__(self,value):
        self.data = value
        self.prev = None
        self.next = None
class doubly:
    def __init__(self):
        self.head =None
        self.tail = None
    def insertAtBeg(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
    def printing(self):
        curr = self.head
        while curr!=None:
            print(curr.data,end= " ")
            curr = curr.next

l = doubly()
l.insertAtBeg(2)
l.insertAtBeg(3)
l.insertAtBeg(4)
l.printing()
        
