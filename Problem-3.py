a = int(input("Enter a number: "))

limit = a if a % 2 == 1 else a - 1   # Only odd range

result = []
for i in range(1, limit + 1, 2):
    result.append(i)

print(*result, sep=", ")
