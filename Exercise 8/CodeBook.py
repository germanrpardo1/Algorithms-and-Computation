### I use another Linked list here
# Every node stores a character ch as an attribute
# Every node stores a codeword that corresponds to the character ch stored
# and next and previous as usual in Linked lists

class Node:
    def __init__(self, ch, codeword):
        self.ch = ch
        self.codeword = codeword
        self.next = None
        self.previous = None

class CodeBook:
    def __init__(self):
        self.head = None
        self.length = 0

    # in this case it is not a sorted linked list, instead it inserts elements in constant time by making the new element the head 
        
    def insert(self, ch, codeword):
        node = Node(ch, codeword)
        
        if self.head == None:
            self.head = node
        else:
            temp = self.head
            temp.previous = node
            node.next = temp
            self.head = node
            
        self.length += 1     
          
    # returns the codeword that correspond to the input character ch        
    def codeFor(self, ch):
        if self.head == None:
            return None
        else:
            node = self.head
            while node.ch != ch and node.next != None:
                node = node.next
            if node.next == None and node.ch != ch:
                return None
            elif node.ch == ch:
                return node.codeword

    
    def __len__(self):
        return self.length
       
    def print(self):
        node = self.head
        while node != None:
            print(node.ch, '->', node.codeword)
            node = node.next