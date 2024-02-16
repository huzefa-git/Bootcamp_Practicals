class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class ll:
    def __init__(self):
        self.head=None
    def insertatbeg(self,data):
        new=node(data)
        if self.head==None:
            self.head=new
        else:
            new.next=self.head
            self.head=new
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

#pasted on linkedlist.py(20_11_23)

