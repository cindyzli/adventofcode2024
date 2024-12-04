with open("input.txt", "r") as file:
    lines = file.readlines()


array_of_lines = [line.strip() for line in lines]

arr_left = []
arr_right = []
for line in array_of_lines:
    x = line.split(" ")
    arr_left.append(int(x[0]))
    arr_right.append(int(x[-1]))


sum = 0
for i in range(len(arr_left)):
    c = arr_right.count(arr_left[i])
    sum += arr_left[i] * c

print(sum)