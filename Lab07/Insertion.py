import json
def InsertionSort(arrey: list, last: int):
    cout = 0
    for i in range(last):
        hold = arrey[i]
        walker = i - 1
        while walker >= 0 and hold < arrey[walker]:
            arrey[walker + 1] = arrey[walker]
            walker -= 1
            cout += 1
        arrey[walker + 1] = hold
        cout += 1
        print(arrey)
    return f"Comparison times: {cout}"
print(InsertionSort(json.loads(input()), int(input())))
