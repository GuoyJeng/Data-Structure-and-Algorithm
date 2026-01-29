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
    def delete(self, data: int):
        def deleteBST(root: BSTNode, dltKey: int):
            if dltKey < root.data:
                return deleteBST(root.left, dltKey)
            elif dltKey > root.data:
                return deleteBST(root.right, dltKey)
            else:
                if root.left == None:
                    root = root.right
                elif root.right == None:
                    root = root.left
                else:
                    save = root
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
    def delete(self, data: int):
        def deleteBST(root: BSTNode, dltKey: int):
            if root is None:
                print("Delete Error, " + str(dltKey) + " is not found in Binary Search Tree.")
                return root
            if dltKey < root.data:
                root.left = deleteBST(root.left, dltKey)
                return root
            elif dltKey > root.data:
                root.right = deleteBST(root.right, dltKey)
                return root
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                check = root.right
                while check.left is not None:
                    check = check.left
                root.data = check.data
                root.right = deleteBST(root.right, check.data)
            return root
        self.root = deleteBST(self.root, data)

def main():
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()

main()
