ex_of_line = "MMMMMMMMMSXSXSMXASAAMAAXAAAMMXMXMAMMMAAAASXMMASAXAXMSMMMSASASXSSMASAMMMMAAMMAXXAXMXMXMXMXSAMXAMASAMAMXMAMSMSMSMXMAMXMMXAAMAAAMXAAAAXSMXSMMXX"
with open("day4/input.txt", "r") as file:
    lines = file.readlines()

char_arr = [list(s) for s in lines]

for i in range(len(char_arr)):
    if len(char_arr[i]) > len(ex_of_line):
        char_arr[i] = char_arr[i][:-1]

counter = 0
def check_surroundings(i, j):
    global counter
    if i-1 in range(len(char_arr)) and j-1 in range(len(ex_of_line)) and i+1 in range(len(char_arr)) and j+1 in range(len(ex_of_line)):
        if (char_arr[i-1][j-1] == 'M' and char_arr[i+1][j+1] == 'S') or (char_arr[i-1][j-1] == 'S' and char_arr[i+1][j+1] == 'M'):
            if (char_arr[i-1][j+1] == 'M' and char_arr[i+1][j-1] == 'S') or (char_arr[i-1][j+1] == 'S' and char_arr[i+1][j-1] == 'M'):
                counter+=1

for i in range(len(char_arr)):
    for j in range(len(char_arr[0])):
        if char_arr[i][j] == 'A':
            check_surroundings(i, j)

print(counter)


