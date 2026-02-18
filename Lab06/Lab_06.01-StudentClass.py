class Student:
    def __init__(self, ID=None, Name=None, GPA=None):
        self.ID = ID
        self.Name = Name
        self.GPA = GPA
    def print_details(self):
        print("ID:", self.ID)
        print("Name:", self.Name)
        print("GPA:", f"{self.GPA:.2f}")
def main(text_in):
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()

main(input())