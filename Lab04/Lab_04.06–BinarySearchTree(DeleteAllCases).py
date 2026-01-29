class BSTNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self) -> bool:
        return self.root is None

    def insert(self, data: int):
        if self.is_empty():
            self.root = BSTNode(data)
        else:
            def _insert(current_node: BSTNode, data: int):
                if (data < current_node.data):
                    if current_node.left is None:
                        current_node.left = BSTNode(data)
                    else:
                        _insert(current_node.left, data)
                else:
                    if current_node.right is None:
                        current_node.right = BSTNode(data)
                    else:
                        _insert(current_node.right, data)
            _insert(self.root, data)

    def preorder(self):
        def traverse(node: BSTNode):
            if node is not None:
                print("->", node.data, end=" ")
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        print()

    def inorder(self):
        def traverse(node: BSTNode):
            if node is not None:
                traverse(node.left)
                print("->", node.data, end=" ")
                traverse(node.right)
        traverse(self.root)
        print()

    def postorder(self):
        def traverse(node: BSTNode):
            if node is not None:
                traverse(node.left)
                traverse(node.right)
                print("->", node.data, end=" ")
        traverse(self.root)
        print()

    def traverse(self):
        if not self.is_empty():
            print("Preorder: ", end="")
            self.preorder()
            print("Inorder: ", end="")
            self.inorder()
            print("Postorder: ", end="")
            self.postorder()
        else:
            print("This is an empty binary search tree.")

    def find_min(self, start: BSTNode) -> BSTNode:
        if start is None:
            return None
        def traverse(node: BSTNode) -> int:
            if node.left is None:
                return node
            else:
                return traverse(node.left)

        return traverse(start)

    # Find the maximum/largest node in the tree
    def find_max(self, start: BSTNode) -> BSTNode:
        if start is None:
            return None
        def traverse(node: BSTNode) -> int:
            if node.right is None:
                return node
            else:
                return traverse(node.right)

        return traverse(start)

    def delete(self, data: int):
        def _delete_node(current_node: BSTNode, data: int) -> BSTNode:
            if current_node is None:
                return None
            elif data < current_node.data:
                current_node.left = _delete_node(current_node.left, data)
            elif data > current_node.data:
                current_node.right = _delete_node(current_node.right, data)
            else:
                if current_node.left is None:
                    return current_node.right
                elif current_node.right is None:
                    return current_node.left
                temp = self.find_max(current_node.left)
                current_node.data = temp.data
                current_node.left = _delete_node(current_node.left, temp.data)

            return current_node
        self.root = _delete_node(self.root, data)

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
