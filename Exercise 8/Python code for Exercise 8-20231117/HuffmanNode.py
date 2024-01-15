# A class representing a node of a Huffman Tree
class HuffmanNode:
    def __init__(self):
        self.label = ""     # a string containing all the characters represented by this node
                            # non-leaf nodes have labels of length > 1
        self.freq = 0.0     # sum of frequencies of all characters represented by this node
        self.left = None    # left child of this node
        self.right = None   # right child of this node
