class Node:
    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None
    
class doublyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtBeg(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def insertAtEnd(self,value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def deletionAtEnd(self):
        curr = self.tail.prev
        curr.next = None
        self.tail = curr

    def printList(self):
        curr = self.head
        while(curr!=None):
            print(curr.data,"->",end="")
            curr = curr.next
        print()
        print(self.head.data)
        print(self.tail.data)

#22-11-23 continuation
    
    def insertatmid(self,value):
        fast = self.head
        slow = self.head
        while(fast.next.next!=None and fast.next!=None):
            fast = fast.next.next
            slow = slow.next
        newnode = Node(value)
        newnode.next = slow.next
        slow.next.prev = newnode
        slow.next = newnode
        newnode.prev = slow 

    def sort(self):
        l = []
        curr = self.head
        while(curr!=None):
            l.append(curr.data)
            curr = curr.next
            l.sort()
        curr = self.head
        i=0
        while curr:
            curr.data = l[i]
            curr = curr.next
            i+=1
        
    def sort1(self):
        l= []
        even=[]
        odd=[]
        curr= self.head
        while(curr!=None):
            if(curr.data%2==0):
                even.append(curr.data)
            else:
                odd.append(curr.data)
            curr = curr.next
        even.sort()
        even = even[::-1]
        odd.sort()
        print(even+odd)
            
l = doublyList()
l.insertAtBeg(1)
l.insertAtBeg(2)
l.insertAtBeg(3)
l.insertAtEnd(5)
l.insertAtEnd(6)
l.insertAtEnd(7)
#l.deletionAtEnd()
l.insertatmid(11)
l.sort()
l.sort1()
l.printList()