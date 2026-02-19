import json
def selectionSort(arrey: list, last: int):
    cout = 0
    current = 0
    while current < last:
        smallest = current
        walker = current + 1
        while walker <= last:
            if arrey[walker][0] < arrey[smallest][0]:
                smallest = walker
            elif arrey[walker][0] == arrey[smallest][0]:
                if int(arrey[walker][1:]) < int(arrey[smallest][1:]):
                    smallest = walker
            walker += 1
            cout += 1
        arrey[current], arrey[smallest] = arrey[smallest], arrey[current]
        current += 1
        print(arrey)
    return f"Comparison times: {cout}"
print(selectionSort(json.loads(input()), int(input())))
