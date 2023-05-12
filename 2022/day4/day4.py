# Read input data
f = open("input4.txt", "r")
data = f.read()

# Part 1
count = 0

for pair in data.split("\n"):
    assignment1 = pair.split(",")[0]
    section1 = set()
    for num in range(
        int(assignment1.split("-")[0]), int(assignment1.split("-")[1]) + 1
    ):
        section1.add(num)

    assignment2 = pair.split(",")[1]
    section2 = set()
    for num in range(
        int(assignment2.split("-")[0]), int(assignment2.split("-")[1]) + 1
    ):
        section2.add(num)

    if section1.issubset(section2) or section2.issubset(section1):
        count += 1

print(count)
