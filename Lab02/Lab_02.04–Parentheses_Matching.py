class ArreyStack:
    def __init__(self):
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Stack"""
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
        """Pop"""
        if self.size == 0:
            print("Underflow: Cannot pop data from an empty list")
            return None
        self.size -= 1
        return self.data.pop()

    def is_empty(self):
        """Is Empty"""
        if self.size == 0:
            return True
        return False

    def get_stack_top(self):
        """Get Stack Top"""
        if self.size == 0:
            print("Underflow: Cannot get stack top from an empty list")
            return None
        return self.data[-1]

    def get_size(self):
        """Get Size"""
        return self.size

def is_parentheses_matching(yes: str):
    stack = ArreyStack()
    check = True
    for char in yes:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.get_size() == 0:
                check = False
            stack.pop()
    if stack.is_empty() and check:
        print(f"Parentheses in {x} are matched")
    else:
        print(f"Parentheses in {x} are unmatched")
        return False
    return stack.is_empty()

x = input()
print(is_parentheses_matching(x))
