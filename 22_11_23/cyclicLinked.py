#previous codes are in 21_11_23
class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class cll:
    def __init__(self):
        self.head = None

    def insertAtBeg(self, value):
        newnode = node(value)
        if self.head ==None:
            self.head = newnode
            newnode.next = self.head
        else:
            curr = self.head
            newnode.next = curr
            while(curr.next!=self.head):
                curr = curr.next
            curr.next = newnode
            self.head = newnode

    def printList(self):
        if not self.head:
            print("Empty list")
            return
        print(self.head.data, end="->")
        curr = self.head.next
        while curr != self.head:
            print(curr.data, "->", end="")
            curr = curr.next
        print()
# Create a circular linked list and insert elements
l = cll()
l.insertAtBeg(1)
l.insertAtBeg(2)
l.insertAtBeg(3)
l.insertAtBeg(4)

# Print the circular linked list
l.printList()