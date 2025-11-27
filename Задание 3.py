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
n = int(input()) #"12"
arr = list(map(int, input().split())) #"1 3 2 4 1 3 2 5 1 3 2 1"

result = []
for i in range(n):
    found = -1
    for j in range(i + 1, n):
        if arr[j] < arr[i]:
            found = arr[j]
            break
    result.append(found)

print(' '.join(map(str, result)))
