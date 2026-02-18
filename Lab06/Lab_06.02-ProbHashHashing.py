class Student:
    def __init__(self, ID, name, GPA):
        self.ID = ID
        self.name = name
        self.GPA = GPA
    def print_details(self):
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"GPA: {self.GPA:.2f}")
class ProbHash:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
    def hash(self, key):
        return key % self.size
    def rehash(self, hkey):
        return (hkey + 1) % self.size
    def insert_data(self, student):
        hash_key = self.hash(student.ID)
        start_key = hash_key
        while self.table[hash_key] is not None:
            hash_key = self.rehash(hash_key)
            if hash_key == start_key:
                print(f"The list is full. {student.ID} could not be inserted.")
                return
        self.table[hash_key] = student
        print(f"Insert {student.ID} at index {hash_key}")
    def search_data(self, std_id):
        hash_key = self.hash(std_id)
        start_key = hash_key
        while self.table[hash_key] is not None:
            if self.table[hash_key].ID == std_id:
                print(f"Found {std_id} at index {hash_key}")
                return self.table[hash_key]
            hash_key = self.rehash(hash_key)
            if hash_key == start_key:
                break
        print(f"{std_id} does not exist.")
        return None
def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
