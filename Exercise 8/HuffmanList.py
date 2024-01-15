from HuffmanNode import *


### This is a node that stores a Huffman Node 
# I created so I can be able to sort the nodes' frequence without modifying the original left and right of the Huffman node
# using left and right just for sorting
class Node:
    def __init__(self, huffNode):
        self.huffNode = huffNode
        self.right = None
        self.left = None

# This is a sorted Linked list.
# It sorts the nodes by their frequency
class HuffmanList:
    def __init__(self):
        self.head = None

    # Insert node with a Huffman Node (that itself have its left and right) and left and right
    # Keeps the nodes sorted by their frequency
    def insert(self, node):
      
        if self.head == None:
            self.head = Node(node)
            
        # Checks the frequency of the Huffman node
        elif self.head.huffNode.freq >= node.freq:   
            node = Node(node)
            
            old_head = self.head
            old_head.right = node
            
            node.left = old_head
            node.right = None
            temp = node
            if self.head != None:
                self.head = temp
            self.head = temp
        else:
            p = self.head
            node = Node(node)
            while p.left != None and p.left.huffNode.freq < node.huffNode.freq:  
                p = p.left
            node.left = p.left
            node.right = p
            temp = node   
            if p.left != None:
                p.left.right = temp
            p.left = temp
            
    # Extracts the head node, which has a Huffman node with minimal frequency and deletes it afterwards     
    def extractMin(self):
        
        min_node = self.head
        new_head = self.head.left
        if len(self) > 1:
            new_head.right = None
            self.head = new_head
        else:
            self.head = None
        return min_node.huffNode

    
    def __len__(self):
        start = self.head
        n = 0
        while start != None:
            start = start.left
            n += 1
        if self.head == None:
            return 0
        return n

    
    def __str__(self):
        if self.head == None:
            return "None"
        s = "None <- "
        p=self.head
        while p.left != None:
            s += str(p.huffNode.freq) + " <-> "
            p = p.left
        s += str(p.huffNode.freq) + " -> None"
        return s