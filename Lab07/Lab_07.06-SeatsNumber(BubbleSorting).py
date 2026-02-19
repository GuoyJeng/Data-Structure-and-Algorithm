import json
def bubbleSort(arrey: list, last: int):
    cout = 0
    current = 0
    check = False
    while current <= last and not check:
        walker = last
        check = True
        while walker > current:
            if arrey[walker][0] < arrey[walker - 1][0]:
                check = False
                arrey[walker], arrey[walker - 1] = arrey[walker - 1], arrey[walker]
            elif arrey[walker][0] == arrey[walker - 1][0]:
                if int(arrey[walker][1:]) < int(arrey[walker - 1][1:]):
                    check = False
                    arrey[walker], arrey[walker - 1] = arrey[walker - 1], arrey[walker]
            walker -= 1
            cout += 1
        current += 1
        print(arrey)
    return f"Comparison times: {cout}"
print(bubbleSort(json.loads(input()), int(input())))
