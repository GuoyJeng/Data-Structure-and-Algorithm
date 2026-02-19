import json
def bubbleSort(arrey: list, last: int):
    cout = 0
    current = 0
    check = False
    while current <= last and not check:
        walker = last
        check = True
        while walker > current:
            if arrey[walker] < arrey[walker - 1]:
                check = False
                arrey[walker], arrey[walker - 1] = arrey[walker - 1], arrey[walker]
            walker -= 1
            cout += 1
        current += 1
        print(arrey)
    return f"Comparison times: {cout}"
print(bubbleSort(json.loads(input()), int(input())))
