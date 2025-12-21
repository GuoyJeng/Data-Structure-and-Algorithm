class ArreyStack:
    def __init__(self, data=[], size=0):
        self.data = data
        self.size = size
    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1
    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.data.pop()
    def get_size(self):
        return self.size
    def is_empty(self):
        if self.size == 0:
            return True
        return False

stack = ArreyStack()
group = [ArreyStack() for _ in range(int(input()))]
num_student = int(input())

for i in range(num_student):
    stack.push(input())

while not stack.is_empty():
    for i in group:
        x = stack.pop()
        i.push(x)

