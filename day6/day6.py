ex_of_line = "...............#.....................#...#..........................................#..........#......#..........................."
with open("day6/input.txt", "r") as file:
    lines = file.readlines()

char_arr = [list(s) for s in lines]
for i in range(len(char_arr)):
    if len(char_arr[i]) > len(ex_of_line):
        char_arr[i] = char_arr[i][:-1]

DELTA = {
    '^': (-1, 0),
    '>': (0, 1),
    "v": (1, 0),
    "<": (0, -1)
}
ROTATE_90 = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^"
}

have_been = set()
found = False
for i in range(len(char_arr)):
    for j in range(len(char_arr[0])):
        if char_arr[i][j] in DELTA:
            guard_i, guard_j = i, j
            direction = char_arr[i][j]
            found = True
            break
    if found:
        break

while (guard_i in range(len(char_arr)) and (guard_j in range(len(char_arr)))):
    print(guard_i, guard_j, direction)
    if char_arr[guard_i][guard_j] == '#':
        guard_i, guard_j = guard_i - DELTA[direction][0], guard_j - DELTA[direction][1]
        direction = ROTATE_90[direction]
    else:
        have_been.add((guard_i, guard_j))
        char_arr[guard_i][guard_j] = 'X'
        guard_i, guard_j = guard_i + DELTA[direction][0], guard_j + DELTA[direction][1]

print(len(have_been))