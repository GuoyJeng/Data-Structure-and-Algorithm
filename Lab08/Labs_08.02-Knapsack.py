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
        return None

def knapsack(amount, itemList: list):
    return

def main():
  import json
  items = []
  num_items = int(input())
  while num_items != 0:
    item_in = json.loads(input())
    items.append(Item(item_in['name'], item_in['price'], item_in['weight']))
    num_items = num_items - 1
    knapsack_capacity = float(input())
    knapsack(items, knapsack_capacity)
main()
