from HuffmanList import HuffmanList
from HuffmanNode import HuffmanNode



### I am using a Python dictionary in this case
class CharacterCounts:
    def __init__(self):
        self.dictionary = {}
        self.totalCount = 0

    def increment(self, ch):
        if ch not in self.dictionary.keys():
            self.dictionary[ch] = 1
            self.totalCount += 1
        else:
            self.dictionary[ch] += 1
            self.totalCount += 1
            
    # The HuffmanList stores nodes wich store Huffman nodes     
    def toHuffmanList(self):
        HuffList = HuffmanList()
        for i in self.dictionary:
            n = HuffmanNode()
            n.label = i
            n.freq = self.dictionary[i] / self.totalCount
            HuffList.insert(n) 
        return HuffList