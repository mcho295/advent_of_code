# Read input data
f = open("input3.txt", "r")
data = f.read()

# Part 1
rucksacks = data.split("\n")
num_rucksacks = len(data.split("\n"))

common_list = []

for idx in range(num_rucksacks):
    length = len(rucksacks[idx]) // 2
    compartment1 = rucksacks[idx][:length]
    compartment2 = rucksacks[idx][length:]

    common = list(set(compartment1).intersection(compartment2))
    common_list.extend(common)

priority = 0

for item in common_list:
    if item.islower():
        priority += ord(item) - 96
    else:
        priority += ord(item) - 38

print(priority)

# Part 2
badge_list = []

for idx in range(0, num_rucksacks, 3):
    badge = list(
        set(set(rucksacks[idx]).intersection(rucksacks[idx + 1])).intersection(
            rucksacks[idx + 2]
        )
    )
    badge_list.extend(badge)

priority = 0

for item in badge_list:
    if item.islower():
        priority += ord(item) - 96
    else:
        priority += ord(item) - 38

print(priority)
