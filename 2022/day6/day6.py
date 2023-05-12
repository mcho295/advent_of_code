# Read input data
f = open("input6.txt", "r")
data = f.read()

# Part 1
for idx in range(len(data) - 3):
    word = set()
    for num in range(4):
        word.add(data[idx + num])

    if len(word) == 4:
        break

print(idx + 4)

# Part 2
for idx in range(len(data) - 13):
    word = set()
    for num in range(14):
        word.add(data[idx + num])

    if len(word) == 14:
        break

print(idx + 14)
