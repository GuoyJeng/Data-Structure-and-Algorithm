class Item:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_weight(self):
        return self.weight
    
    def get_cost(self):
        return self.price / self.weight

def knapsack(items: list, capacity: float):
    n = len(items)
    data = [[0] * (int(capacity) + 1) for _ in range(n)]

    items.sort(key=lambda x: x.get_cost(), reverse=True)

    for i in range(n):
        for j in range(int(capacity) + 1):
            if j >= items[i].get_weight():
                data[i][j] = max(data[i - 1][j], items[i].get_price() + data[i - 1][j - int(items[i].get_weight())])

    total_value = 0
    current_weight = 0
    selected_items = []

    for item in items:
        if current_weight + item.weight <= capacity:
            selected_items.append(item)
            current_weight += item.weight
            total_value += item.price

    print(f"Knapsack Size: {capacity} kg")
    print("===============================")
    for item in selected_items:
        w = item.weight
        w_display = int(w) if w == int(w) else w
        print(f"{item.name} -> {w_display} kg -> {item.price} THB")
    return total_value

def main():
    import json
    items = []
    num_items = int(input())
    while num_items != 0:
        item_in = json.loads(input())
        items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
        num_items = num_items - 1
    knapsack_capacity = float(input())
    result = knapsack(items, knapsack_capacity)
    print(f"Total: {result} THB")

main()
