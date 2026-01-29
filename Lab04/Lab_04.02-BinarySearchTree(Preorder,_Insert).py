class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root: BSTNode = None
    def is_empty(self):
        if self.root == None:
            return True
        return False
    def insert(self, data: int):
        pNew = BSTNode(data)
        if self.root == None:
            self.root = pNew
            return
        p = self.root
        while p != None:
            if data < p.data:
                if p.left == None:
                    p.left = pNew
                    break
                p = p.left
            else:
                if p.right == None:
                    p.right = pNew
                    break
                p = p.right
    def preorder(self):
        def check(node: BSTNode):
            if node != None:
                print(" -> " + str(node.data), end="")
                check(node.left)
                check(node.right)
        check(self.root)
        print()
            
def main():
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    
    print("Preorder:", end="")
    my_bst.preorder()

main()
