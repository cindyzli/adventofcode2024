with open("day2/input.txt", "r") as file:
    lines = file.readlines()


array_of_lines = [line.strip() for line in lines]

num_array = []
for line in array_of_lines:
    arr = line.split(" ")
    num_array.append(arr)

counter = 0

for record in num_array:
    works_for_one = False
    for i in range(len(record) + 1):
        asc = True
        is_valid = True
        last_val = 0
        if i <= len(record):
            modified_record = record[:i] + record[i+1:]
        else:
            modified_record = record
        for i in range(len(modified_record)):
            if i == 0:
                last_val = int(modified_record[i])
            elif i == 1:
                if int(modified_record[i]) < last_val:
                    asc = False
                if last_val == int(modified_record[i]):
                    is_valid= False

            if not i == 0:
                if asc:
                    if int(modified_record[i]) <= last_val or int(modified_record[i]) - 3 > last_val:
                        is_valid = False
                else:
                    if int(modified_record[i]) >= last_val or int(modified_record[i]) + 3 < last_val:
                        is_valid = False
                last_val = int(modified_record[i])

        if is_valid:
            works_for_one = True
    if works_for_one:
        counter += 1
print(counter)



