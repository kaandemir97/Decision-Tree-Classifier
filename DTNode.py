class Node:
    def __init__(self, att, left, right):
        self.att = att
        self.left = left
        self.right = right
        return
    def report(self, indent):
        print("%s%s = True:\n" % (indent, self.att))
        self.left.report(indent+"  ")
        print("%s%s = False:\n"% (indent, self.att))
        self.right.report(indent+"  ")
        return
    def isLeafNode(self):
        return False

class LeafNode:
    def __init__(self, att, probability):
        self.att = att
        self.probability = probability
        return
    def report(self, indent):
        print("%sClass %s, prob = %4.2f\n"%(indent, self.att, float(self.probability)))
        return
    def isLeafNode(self):
        return True

###DTNODE.py CONTAINS LEAF AND REGULAR NODE
###REPORT FUNCTION CALLED BY ABSTRACTED RECURSIVE WRAPPER - PRINTS LEARNT TREE
