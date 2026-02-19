import json
def InsertionSort(arrey: list, last: int):
    cout = 0
    current = 1
    while current <= last:
        key = arrey[current]
        walker = current - 1
        while walker >= 0 and arrey[walker] > key:
            cout += 1
            arrey[walker + 1] = arrey[walker]
            walker -= 1
        arrey[walker + 1] = key
        current += 1
        print(arrey)
    return f"Comparison times: {cout}"
print(InsertionSort(json.loads(input()), int(input())))
