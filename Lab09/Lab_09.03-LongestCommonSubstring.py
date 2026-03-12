x = input().strip()
y = input().strip()

prev = [0] * len(x)

num = 0
end = 0

for i in range(len(x)):
    current = [0] * len(y)
    for j in range(len(y)):
        if x[i] == y[j]:
            current[j] = prev[j - 1] + 1
            if current[j] > num:
                num = current[j]
                end = i
    prev = current
    
ans = x[end - num + 1: end + 1]
print(f"{ans}\n{len(ans)}" if ans else "No common substring.")
