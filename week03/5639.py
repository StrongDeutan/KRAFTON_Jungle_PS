import sys
sys.setrecursionlimit(10010)
class node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class tree:
    def __init__(self, root: node):
        self.root = root

    def insert_node(self, curNode: node, v):
        if(v < curNode.value):
            if(curNode.left_child == None):
                curNode.left_child = node(v)
                curNode = self.root
                return
            else:
                self.insert_node(curNode.left_child, v)
        else:
            if(curNode.right_child == None):
                curNode.right_child = node(v)
                curNode = self.root
                return
            else:
                self.insert_node(curNode.right_child, v)

    def post_order(self, cur: node):
        if(cur.left_child != None):
            self.post_order(cur.left_child)
        if(cur.right_child != None):
            self.post_order(cur.right_child)
        print(cur.value)
        return


n = int(sys.stdin.readline())
r = node(n)
t = tree(r)
while(1):
    try:
        n = int(sys.stdin.readline())
        if(n == -1):
            break
        n = int(n)
        t.insert_node(t.root, n)
    except:
        break;
t.post_order(t.root)