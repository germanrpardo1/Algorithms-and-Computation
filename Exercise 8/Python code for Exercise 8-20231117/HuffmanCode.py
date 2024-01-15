from HuffmanTree import HuffmanTree
from CodeBook import CodeBook
from HuffmanNode import HuffmanNode
from math import log2,ceil

# A class for generating a Huffman tree and a corresponding Huffman code
# for a given word.
class HuffmanCode:
    def __init__(self,word):
        self.tree = HuffmanTree(word)                      # Huffman tree is constructed
        self.book = CodeBook()                             # Code book is initialised 
        self.generateCode()                                # Code is generated

    def generateCode(self):
        self.generateCodeRec("",self.tree.root)            # the root corresponds to empty prefix

    # generate the codewords recursively
    def generateCodeRec(self,prefix,node):
        if node==None:
            return
        if len(node.label)==1:                             # current node is leaf, insert codeword
            self.book.insert(node.label[0],prefix)
        else:
            self.generateCodeRec(prefix+"0",node.left)     # add 0 for going down to left subtree
            self.generateCodeRec(prefix+"1",node.right)    # add 1 for going down to right subtree

    # encode word by looking up the codeword for each character
    def encode(self,word):                                 
        encoding = ""
        for ch in word:
            encoding += self.book.codeFor(ch)
        return encoding

    # print the code book
    def printCode(self):
        self.book.print()

    # print the Huffman tree
    def printTree(self):
        self.tree.print()

    # returns the number of characters in the code book
    def __len__(self):
        return len(self.book)



if __name__ == "__main__":
    
    word = "a small test case"
    # word = "mississippi"
    mycode = HuffmanCode(word)
    print("The Huffman tree for the string \"",word,"\":",sep='')
    mycode.printTree()
    print()
    print("The corresponding code:")
    mycode.printCode()
    bits = len(mycode.encode(word))
    print()
    print("The Huffman encoding of \"", word,"\" uses ", bits," bits.",sep='')
    bits = 0
    if len(mycode):
        bits = ceil(log2(len(mycode))) * len(word)
    print("Encoding this with a fixed-width code would need", bits, "bits.")


'''
Example output:
python HuffmanCode.py

The Huffman tree for the string "a small test case" :
1.0 ( sltemca  )
    0.4117647058823529 ( slt )
        0.17647058823529413 ( s )
        0.23529411764705882 ( lt )
            0.11764705882352941 ( l )
            0.11764705882352941 ( t )
    0.5882352941176471 ( emca  )
        0.23529411764705882 ( emc )
            0.11764705882352941 ( e )
            0.11764705882352941 ( mc )
                0.058823529411764705 ( m )
                0.058823529411764705 ( c )
        0.35294117647058826 ( a  )
            0.17647058823529413 ( a )
            0.17647058823529413 (   )

The corresponding code:
s -> 00
l -> 010
t -> 011
e -> 100
m -> 1010
c -> 1011
a -> 110
  -> 111

The Huffman encoding of "a small test case" uses 50 bits.
Encoding this with a fixed-width code would need 51 bits.
'''
