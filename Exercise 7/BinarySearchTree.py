class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val
        
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # returns the minimum , which is in the left - most item 
    # returns None if the tree is empty
    def min(self):
        node = self.root
        if self.root:
            return None
        else:
            while node:
                node = node.left
            return node
        
    # inserts x in the tree unless present
    # returns pointer to Node with value x
    def insert(self, x):
        y = None
        node = self.root
        
        while node:
            y = node
            if x.value < node.value:
                node = node.left
            else:
                node = node.right
        #p = y
        if not y:
            self.root = x
        elif x.value < y.value:
            y.left = x
        else:
            y.right = x
            
        return y
        

    # finds value x in the tree , returns Node containing it;
    # if not present , returns None
    def find (self, x) :
        node = self.root
 
        while node != None:
            if node.value == x:
                return node
            if node.value < x:
                node = node.right
            else:
                node = node.left
        return node
    