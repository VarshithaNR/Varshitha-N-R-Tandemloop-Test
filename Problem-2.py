a = int(input("Enter a number: "))

result = []
for i in range(1, a + 1):
    result.append(2 * i - 1)

print(*result, sep=", ")
