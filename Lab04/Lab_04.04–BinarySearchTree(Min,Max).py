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
    def find_min(self):
        def check_min(node: BSTNode):
            if node.left == None:
                return node.data
            else:
                return check_min(node.left)
        return check_min(self.root)
    def find_max(self):
        def check_max(node: BSTNode):
            if node.right == None:
                return node.data
            else:
                return check_max(node.right)
        return check_max(self.root)  
    def preorder(self):
        def check_preorder(node: BSTNode):
            if node != None:
                print("->", node.data, end=" ")
                check_preorder(node.left)
                check_preorder(node.right)
        check_preorder(self.root)
        print()
    def inorder(self):
        def check_inorder(node: BSTNode):
            if node != None:
                check_inorder(node.left)
                print("->", node.data, end=" ")
                check_inorder(node.right)
        check_inorder(self.root)
        print()
    def postorder(self):
        def check_postorder(node: BSTNode):
            ans = ""
            if node != None:
                check_postorder(node.left)
                check_postorder(node.right)
                print("->", node.data, end=" ")
        check_postorder(self.root)
        print()
    def traverse(self):
        if not self.is_empty():
          print(f"Preorder: ", end="")
          self.preorder()
          print(f"Inorder: ", end="")
          self.inorder()
          print(f"Postorder: ", end="")
          self.postorder()
        else:
            print("This is an empty binary search tree.")

def main():
  my_bst = BST()
  for i in range(int(input())):
    my_bst.insert(int(input()))
  my_bst.traverse()
  print("Max:", my_bst.find_max())
  print("Min:", my_bst.find_min())

main()