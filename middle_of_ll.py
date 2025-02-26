#Node class to create new node
class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

#LinkedList class without length 
class LinkedList:
    def __init__(self, value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
    
    def append(self, value):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
        return True
    
    def find_middle_node(self):
        slow=self.head
        fast=self.head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        return slow
    
myLinkedList=LinkedList(5)
myLinkedList.append(10)
myLinkedList.append(15)
myLinkedList.append(20)
myLinkedList.append(25)
myLinkedList.append(30)

print(myLinkedList.find_middle_node().value)
