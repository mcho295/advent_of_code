# Read input data
f = open("input1.txt", "r")
data = f.read()

# Part 1
calorie_list = []
num_elves = len(data.split("\n\n"))

for elf in range(num_elves):
    sum_calorie = 0
    for calorie in data.split("\n\n")[elf].split("\n"):
        sum_calorie += int(calorie)

    calorie_list.append(sum_calorie)

print(max(calorie_list))

# Part 2
calorie_list = sorted(calorie_list, reverse=True)
print(sum(calorie_list[0:3]))
