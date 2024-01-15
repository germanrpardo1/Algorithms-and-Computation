from HuffmanNode import HuffmanNode
from HuffmanList import HuffmanList
from CharacterCounts import CharacterCounts

# A class for representing a Huffman tree, implemented as a binary tree
# whose nodes are of type HuffmanNode
class HuffmanTree:
    def __init__(self,word):
        self.root = None                               # root of the tree
        counts = CharacterCounts()                     # count occurences of each character in word
        for ch in word:
            counts.increment(ch)
        list = counts.toHuffmanList()                  # create a HuffmanList from these counts
        while len(list)>1:                             # Apply the (greedy) Huffman algorithm
            nd = HuffmanNode()                         # to build the Huffman tree
            nd.left = list.extractMin()                # by repeatedly combining two lowest frequency nodes
            nd.right = list.extractMin()
            nd.freq = nd.left.freq + nd.right.freq
            nd.label = nd.left.label + nd.right.label
            list.insert(nd)
        self.root = list.extractMin()

    # Print the Huffman tree
    def print(self):
        self.printRecursively(self.root,0)

    # recursive printing of the Huffman tree
    # depth is the depth the current node nd in the tree for correct indentation
    def printRecursively(self,nd,depth):
        if nd == None:
            return
        print("    "*depth,end='')              # indentation based on depth of printed node
        print(nd.freq,end=' ')
        print("(",nd.label,")")
        self.printRecursively(nd.left, depth+1)
        self.printRecursively(nd.right, depth+1)
