from collections import defaultdict

# Read input data
f = open("input5.txt", "r")
data = f.read()

# Part 1
diagram = data.split("\n\n")[0].split("\n")
crates = defaultdict(list)

for row in range(len(diagram)):
    for idx, char in enumerate(diagram[row]):
        if char.isalpha():
            crates[idx // 4 + 1].insert(0, char)

procedures = data.split("\n\n")[1].split("\n")

for idx in range(len(procedures)):
    procedure = procedures[idx].split()
    amount, source, target = int(procedure[1]), int(procedure[3]), int(procedure[5])
    for num in range(amount):
        moved = crates[source].pop()
        crates[target].append(moved)

result = list(crates.items())
result = sorted(result, key=lambda x:x[0])
top = ''.join([x[1][-1] for x in result])

print(top)
