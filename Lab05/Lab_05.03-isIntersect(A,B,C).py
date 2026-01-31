import json as js
def isIntersect(a: set, b: set, c: set):
    check = a.intersection(b)
    if check.intersection(c):
        return True
    return False
print(isIntersect(set(js.loads(input())), set(js.loads(input())), set(js.loads(input()))))