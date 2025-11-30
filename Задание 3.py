#Получение ПСП
s = input().strip() # "))))((((()()"

count = 0
result = 0

for char in s:
    if char == '(':
        count += 1
    else:
        if count > 0:
            count -= 1
        else:
            result += 1

result += count
print(result)

#Ближайший меньший

n = int(input())
arr = list(map(int, input().split()))
result = [-1] * n
stack = []

for i in range(n):
    while stack and arr[i] < arr[stack[-1]]:
        pos = stack.pop()
        result[pos] = arr[i]
    stack.append(i)

print(' '.join(map(str, result)))
