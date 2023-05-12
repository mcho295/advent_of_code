# Read input data
f = open("input3.txt", "r")
data = f.read()

# Part 1
num_rucksacks = len(data.split("\n"))

common_list = []

for rucksack in range(num_rucksacks):
    length = len(data.split("\n")[rucksack]) // 2
    compartment1 = data.split("\n")[rucksack][:length]
    compartment2 = data.split("\n")[rucksack][length:]

    common = list(set(compartment1).intersection(compartment2))
    common_list.extend(common)

priority = 0

for item in common_list:
    if item.islower():
        priority += ord(item) - 96
    else:
        priority += ord(item) - 38

print(priority)
