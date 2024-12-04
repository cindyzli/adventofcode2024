ex_of_line = "MMMMMMMMMSXSXSMXASAAMAAXAAAMMXMXMAMMMAAAASXMMASAXAXMSMMMSASASXSSMASAMMMMAAMMAXXAXMXMXMXMXSAMXAMASAMAMXMAMSMSMSMXMAMXMMXAAMAAAMXAAAAXSMXSMMXX"
with open("day4/input.txt", "r") as file:
    lines = file.readlines()

char_arr = [list(s) for s in lines]

for i in range(len(char_arr)):
    if len(char_arr[i]) > len(ex_of_line):
        char_arr[i] = char_arr[i][:-1]

# pythonic code!!
directions = [
    (-1,  0, "VBACK"),   
    ( 1,  0, "VFOR"),   
    ( 0, -1, "HBACK"),   
    ( 0,  1, "HFOR"),    
    (-1, -1, "DLBACK"),  
    ( 1,  1, "DLFOR"),   
    (-1,  1, "DRBACK"),
    ( 1, -1, "DRBACK")
]

counter = 0
def check_surroundings(last_seen, i, j, orientation):
    global counter
    if last_seen == "X":
        for di, dj, direction in directions:
            xi, xj = i + di, j + dj
            if xi in range(len(char_arr)) and xj in range(len(ex_of_line)) and char_arr[xi][xj] == 'M':
                check_surroundings('M', xi, xj, direction)
    elif last_seen == "M":
        for di, dj, direction in directions:
            if direction == orientation:
                xi, xj = i + di, j + dj
                if xi in range(len(char_arr)) and xj in range(len(ex_of_line)) and char_arr[xi][xj] == 'A':
                    check_surroundings('A', xi, xj, direction)
    else: # See 'A'
         for di, dj, direction in directions:
            if direction == orientation:
                xi, xj = i + di, j + dj
                if xi in range(len(char_arr)) and xj in range(len(ex_of_line)) and char_arr[xi][xj] == 'S':
                    counter += 1

for i in range(len(char_arr)):
    for j in range(len(char_arr[0])):
        if char_arr[i][j] == 'X':
            check_surroundings('X', i, j, "DUMMY")

print(counter)


