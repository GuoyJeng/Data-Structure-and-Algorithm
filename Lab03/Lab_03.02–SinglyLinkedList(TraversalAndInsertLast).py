class DataNode:
    def __init__(self, data=""):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None
    def traverse(self):
        check = self.head
        ans = ""
        if not check:
            print("This is an empty list.")
        else:
            while check != None:
                ans += str(check.data).strip() + " -> "
                check = check.next
            print(ans.rstrip(" -> "))
    def insert_last(self, data):
        pNew = DataNode(data)
        if not self.head:
            self.head = pNew
        else:
            start = self.head
            while start.next != None:
                start = start.next
            start.next = pNew
    def insert_front(self):
        return
    def insert_before(self):
        return
    def delete(self):
        return

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    mylist.insert_last(input())
  mylist.traverse()

main()