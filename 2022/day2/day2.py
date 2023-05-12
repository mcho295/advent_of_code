# Read input data
f = open("input2.txt", "r")
data = f.read()

# Part 1
num_games = len(data.split("\n"))
shape_map = {"X": 1, "Y": 2, "Z": 3}
outcome_map = {
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("C", "Y"): 0,
    ("A", "X"): 3,
    ("B", "Y"): 3,
    ("C", "Z"): 3,
    ("A", "Y"): 6,
    ("B", "Z"): 6,
    ("C", "X"): 6,
}

score = 0

for game_num in range(num_games):
    game = data.split("\n")[game_num].split()
    score += shape_map[game[1]]
    score += outcome_map[tuple(game)]

print(score)

# Part 2
shape_map2 = {
    ("A", "Y"): 1,
    ("B", "X"): 1,
    ("C", "Z"): 1,
    ("A", "Z"): 2,
    ("B", "Y"): 2,
    ("C", "X"): 2,
    ("A", "X"): 3,
    ("B", "Z"): 3,
    ("C", "Y"): 3,
}
outcome_map2 = {"X": 0, "Y": 3, "Z": 6}

score = 0

for game_num in range(num_games):
    game = data.split("\n")[game_num].split()
    score += shape_map2[tuple(game)]
    score += outcome_map2[game[1]]

print(score)
