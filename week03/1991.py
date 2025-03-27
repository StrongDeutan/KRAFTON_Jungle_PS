import sys

class node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    
    
class binary_tree:
    def __init__(self, n):
        self.nodeList = []
        for i in range(n):
            newNode = node(i)
            self.nodeList.append(newNode)

        for i in range(n):
            iput = sys.stdin.readline().split()
            parent = int(ord(iput[0])) - 65
            left_child = int(ord(iput[1])) - 65
            right_child = int(ord(iput[2])) - 65

            parent = self.nodeList[parent]
            if(left_child >= 0):
                left_child = self.nodeList[left_child]
                parent.left = left_child
            if(right_child >= 0):
                right_child = self.nodeList[right_child]
                parent.right = right_child

    def pre_order(self, cur: node):
        if(cur == None):
            return
        
        print(chr(cur.val + 65), end="")
        self.pre_order(cur.left)
        self.pre_order(cur.right)


    def mid_order(self, cur: node):
        if(cur == None):
            return
        
        self.mid_order(cur.left)
        print(chr(cur.val + 65), end="")
        self.mid_order(cur.right)
            
    def post_order(self, cur: node):
        if(cur == None):
            return
        
        self.post_order(cur.left)
        self.post_order(cur.right)
        print(chr(cur.val + 65), end="")









n = int(sys.stdin.readline())

bt = binary_tree(n)
bt.pre_order(bt.nodeList[0])
print()
bt.mid_order(bt.nodeList[0])
print()
bt.post_order(bt.nodeList[0])
print()