class Node:
    def __init__(self, item, next, prev):
        self.item = item
        self.next = next
        self.prev = prev
        
        
class Sdll:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        string = 'None'
        node = self.head
        while node.next != None:
            string = string + ',' + str(node.item)
            node = node.next
        string = string + ',' + str(node.item) + ',' + 'None'
        return string
        
    def reverseString(self):
        str_list = ''
        for i in reversed(self.__str__()):
            str_list = str_list + i
       
        return str_list
    
    def isEmpty(self):
        return self.head == None
    ################ No funciona en casos extremos como las esquinas
    def delete(self, x):
               
        actual = self.head
        
        while actual.item != x:
            actual = actual.next
            if actual != self.head:
                past = actual.prev
            
        final = actual
        while final.item == x:
            final = final.next
       
        temp = past
      
        past.prev.next = final
        final.prev = temp
        
        
    def insert(self, x):        
        if self.isEmpty():
            self.tail = Node(x, None, None)
            self.head = Node(x, None, None)

        else:
            
            actual = self.head
            temp = self.head.next

            do = True
            while do:
                ################ No funciona en casos extremos como las esquinas
                if x == actual.item:                    
                    if actual != self.tail:
                        actual.next = Node(x, temp, actual)
                        temp.prev = Node(x, temp.next, actual.next)
                    else:
                        temp2 = actual.prev
                        self.tail.prev = Node(x, self.tail, temp2)
                        temp2.next = Node(x, actual.prev, temp2.prev)
                    do = False
                    
                elif x < self.head.item:
                    self.head = Node(x, actual, None)
                    actual.prev = self.head
                    do = False
                    
                elif temp == None and actual.item > x:
                    self.head = Node(x, actual, None)
                    actual.prev = self.head
                    self.tail = actual
                    do = False
                
                elif temp == None and actual.item < x:
                    actual.next = Node(x, None, actual)
                    self.tail = actual.next
                    do = False      
                    
                elif x > actual.item and x < temp.item:
                    actual.next = Node(x, temp, actual)
                    temp.prev = Node(x, temp, actual)
                    do = False
                    
                else:
                    actual = actual.next
                    temp = temp.next 