def convert_key(data):
    """JSON"""
    return {int(k): v for k, v in data.items()}

def main(num: int):
    import json
    data = convert_key(json.loads(input()))
    print(f"Amount: {num}")
    check = [i for i in data]
    index = 0
    while num:
        if num >= data[check[index]] and data[check[index]]:
            if num // check[index] > data[check[index]]:
                num -= data[check[index]] * check[index]
                data[check[index]] = 0
            else:
                data[check[index]] = data[check[index]] - num // check[index]
                num -= (num // check[index]) * check[index]
        print(num, check[index], data[check[index]])
        index += 1
        if index == len(check):
            break
    if num:
        print("Can not exchange.")
    else:
        for i in check:
            print(f"{i}: {data[i]}")
main(int(input()))
