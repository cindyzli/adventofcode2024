with open("day7/input.txt", "r") as file:
    lines = file.readlines()

def is_possible(goal, nums, ongoing):
    if len(nums) == 1:
        if ongoing + int(nums[0]) == goal or ongoing * int(nums[0]) == goal or goal == int(str(ongoing) + nums[0]):
            return goal
        else:
            return 0
    else:
        return max(is_possible(goal, nums[1:], ongoing + int(nums[0])), 
                   is_possible(goal, nums[1:], ongoing * int(nums[0])),
                   is_possible(goal, nums[1:], int(str(ongoing) + (nums[0]))))

total = 0
for line in lines:
    index_colon = line.find(":")
    goal = int(line[:index_colon])
    nums = line[(index_colon+2):].split(" ")
    if "\n" in nums[-1]:
        nums[-1] = nums[-1][:-1]
    total += is_possible(goal, nums, 0)

print(total)