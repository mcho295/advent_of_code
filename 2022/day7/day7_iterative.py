from collections import defaultdict

# Read input data
f = open("input7.txt", "r")
data = f.read()

# Part 1
commands = data.split("\n")

dir_stack = []
size_map = defaultdict(int)

for command in commands:
    comp = command.split()
    if comp[0] == "$":
        if comp[1] == "cd":
            if comp[2] != "..":
                if len(dir_stack) > 0:
                    dir_stack.append(dir_stack[-1] + "\\" + comp[2])
                else:
                    dir_stack.append(comp[2])
            else:
                dir_stack.pop()
    else:
        if comp[0] != "dir":
            for dir in dir_stack:
                size_map[dir] += int(comp[0])

answer = 0

for dir, size in size_map.items():
    if size <= 100000:
        answer += size

print(answer)
