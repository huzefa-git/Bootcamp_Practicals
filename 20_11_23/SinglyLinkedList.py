class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def traverse(self):
        s= ""
        curr = self.head
        while(curr!=None):
            s = s+str(curr.data)
            curr = curr.next
        print(s)
    
    def __init__(self):
        self.head = None
        self.c = 0
    def insertAtBeg(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    def printList(self):
        curr = self.head
        while(curr!=None):
            print(curr.data,"->",end="")
            curr = curr.next
        print("none")

    def insertAtEnd(self,data):
        newnode = node(data)
        if self.head == None:
            self.head = newnode
        else:
            curr =self.head
            while(curr.next!=None):
                curr = curr.next
            curr.next = newnode

    def insertAtMid(self,data):
        curr=self.head
        while(curr!=None):
            self.c+=1
            curr = curr.next
        print(self.c)
        curr = self.head
        newnode=node(data)
        i=1
        print(self.c//2)
        while(i<self.c//2):
            curr = curr.next
            i+=1
        newnode.next = curr.next
        curr.next = newnode

    def search(self,val,element):
        curr=self.head
        while(curr):
            if curr.data!=val:
                curr=curr.next
            else:
                newnode=node(element)
                newnode.next=curr.next
                curr.next = newnode
                break
    def deleteAtBeg(self):
        if self.head==None:
            print("is empty")
        else:
            curr = self.head
            self.head = curr.next

    def deleteAtEnd(self):
        if self.head == None:
            print("is empty")
        else:
            curr = self.head
            if curr.next ==None:
                self.head = curr.next
            else:
                while(curr.next.next!=None):
                    curr = curr.next
                curr.next = None
    def deleteAtMiddile(self):
        curr=self.head
        while(curr!=None):
            self.c+=1
            curr = curr.next
        print(self.c)
        curr = self.head

        i=1
        print(self.c//2)
        while(i<self.c//2):
            curr = curr.next
            i+=1
        curr.next = curr.next.next
    
    def search1(self,value):#for deletion
        curr=self.head
        while(curr!=None):
            if curr.data!=value:
                curr=curr.next
            else:
                curr.next = curr.next.next
                break
        
l = linkedlist()
l.insertAtBeg(1)
l.insertAtBeg(2)
l.insertAtBeg(3)
# l.insertAtBeg(4)
# l.insertAtBeg(5)
# l.insertAtBeg(6)
# l.insertAtBeg(7)
# l.insertAtBeg(8)
# l.insertAtBeg(9)
# l.insertAtBeg(10)
# l.insertAtBeg(11)
# l.search1(3)
l.printList()