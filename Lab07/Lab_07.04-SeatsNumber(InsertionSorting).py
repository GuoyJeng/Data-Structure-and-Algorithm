import json
def InsertionSort(arrey: list, last: int):
    cout = 0
    current = 1
    while current <= last:
        key = arrey[current]
        walker = current - 1
        while walker >= 0:
            cout += 1
            if key[0] < arrey[walker][0]:
                arrey[walker + 1] = arrey[walker]
                walker -= 1
            elif key[0] == arrey[walker][0]:
                if int(key[1:]) < int(arrey[walker][1:]):
                    arrey[walker + 1] = arrey[walker]
                    walker -= 1
                else:
                    break
            else:
                break
        arrey[walker + 1] = key
        current += 1
        print(arrey)
    return f"Comparison times: {cout}"
print(InsertionSort(json.loads(input()), int(input())))
