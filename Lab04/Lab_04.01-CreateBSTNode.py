class BSTNode:
    def __init__(self, data: int=None):
        """ > w < """
        self.data = data
        self.left = None
        self.right = None

ans = BSTNode(int(input()))
print(ans.data)
print(ans.left)
print(ans.right)