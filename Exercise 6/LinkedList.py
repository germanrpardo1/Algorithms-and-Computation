class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self,item):
        if self.isEmpty():
            self.tail = Node(item, None)
            self.head = Node(item, None)
        else:
            temp = Node(item,self.head)
            self.head = temp
    
    def remove(self):
        temp = self.head.next
        next_n = temp.next
        self.head = Node(temp.item, next_n)
        
    def removeAtEnd(self):
        tail_node = self.tail
        temp = self.head
        do = True
        while do:
            actual = temp
            next_it = temp.next
            if next_it.item == tail_node.item and next_it.next == None:
                actual.next = None
                self.tail = actual
                do = False
            else:
                temp = actual.next
            
            