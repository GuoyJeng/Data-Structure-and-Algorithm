def convert_key(data):
  """JSON"""
  return {int(k): v for k, v in data.items()}

def main(num: int):
  import json
  data = convert_key(json.loads(input()))
  print(f"Amount: {num}")
  ten = data[10]
  five = data[5]
  two = data[2]
  one = data[1]
  while num:
    if num >= 10 and data[10]:
      if num // 10 > data[10]:
        num -= data[10] * 10
        data[10] = 0
        continue
      data[10] = data[10] - num // 10
      num = num % 10
    if num >= 5 and data[5]:
      if num // 5 > data[5]:
        num -= data[5] * 5
        data[5] = 0
        continue
      data[5] = data[5] - num // 5
      num = num % 5
    if num >= 2 and data[2]:
      if num // 2 > data[2]:
        num -= data[2] * 2
        data[2] = 0
        continue
      data[2] = data[2] - num // 2
      num = num % 2
    if num >= 1 and data[1]:
      if num > data[1]:
        num -= data[1]
        data[1] = 0
        break
      data[1] = data[1] - num
      num = 0
  if not num:
    print("Coin exchange result:")
    print(f"  10 baht = {ten - data[10]} coins")
    print(f"  5 baht = {five - data[5]} coins")
    print(f"  2 baht = {two - data[2]} coins")
    print(f"  1 baht = {one - data[1]} coins")
    print(f"Number of coins: {sum([ten, five, two, one]) - sum([data[10], data[5], data[2], data[1]])}")
  else:
    print("Coins are not enough.")
main(int(input()))
