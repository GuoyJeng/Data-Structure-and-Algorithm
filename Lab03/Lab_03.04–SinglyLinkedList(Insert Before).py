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
    def insert_front(self, data):
        pNew = DataNode(data)
        if not self.head:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
            self.count += 1
    def insert_before(self, node, data):
        pNew = DataNode(data)
        if not self.head:
            print("Cannot insert, " + node + " does not exist.")
        elif self.head.data == node:
            self.insert_front(data)
            return
        else:
            prev = None
            start = self.head
            while start.data != node:
                if start.next == None:
                    print("Cannot insert, " + node + " does not exist.")
                    return
                prev = start
                start = start.next
            pNew.next = start
            prev.next = pNew
    def delete(self, data):
        if not self.head:
            print("Cannot delete, " + data + " does not exist.")
        elif self.head.data == data:
            self.head = self.head.next
            return
        else:
            prev = None
            start = self.head
            while start.data != data:
                if start.next == None:
                    print("Cannot delete, " + data + " does not exist.")
                    return
                prev = start
                start = start.next
            prev.next = start.next

def main():
  mylist = SinglyLinkedList()
  for _ in range(int(input())):
    text = input()
    condition, data = text.split(": ")
    if condition == "F":
      mylist.insert_front(data)
    elif condition == "L":
      mylist.insert_last(data)
    elif condition == "B":
        mylist.insert_before(*data.split(", "))
    elif condition == "D":
        mylist.delete(data)
    else:
      print("Invalid Condition!")
  mylist.traverse()

main()