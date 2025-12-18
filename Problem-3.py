a = int(input("Enter a number: "))

count = a if a % 2 != 0 else a - 1

result = []
for i in range(count):
    if i % 2 == 0:
        result.append(2 * (i // 2) + 1)

print(", ".join(map(str, result)))
