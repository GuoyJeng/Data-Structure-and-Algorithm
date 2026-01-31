x = int(input())
num = 0
for i in range(1, x + 1):
    num += len(str(i))
print(num + x)