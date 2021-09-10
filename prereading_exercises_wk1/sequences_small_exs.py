# Small Exercises for Sequences

# 1. Sum the Numbers
# Create a list of numbers, print their sum.

nums_list = [12, 14, -10, 7, 5, 1, 11, 36, -1, 19, 41, 22, 16, 91]
sum = 0

for num in nums_list:
    sum += num
print(sum)

print("-----")

# 2. Largest Number
# Create a list of numbers, print the largest of the numbers.

max_num = max(nums_list)
print(max_num)

print("-----")

# 3. Smallest Number
# Create a list of numbers, print the smallest of the numbers.

min_num = min(nums_list)
print(min_num)

print("-----")
# 4. Even Numbers
# Create a list of numbers, print each number in the list that is even.

for num in nums_list:
    if (num % 2 == 0):
        print(num)

print("-----")

# 5. Positive Numbers
# Create a list of numbers, print each number in the list that is greater than zero.

for num in nums_list:
    if (num > 0):
        print(num)

print("-----")

# 6. Positive Numbers II
# Create a list of numbers, create a new list which contains every number in the given list which is positive.

pos_nums = []

for num in nums_list:
    if (num > 0):
        pos_nums.append(num)
print(pos_nums)

print("-----")

# 7. Multiply a list
# Create a list of numbers, and a single factor (also a number), 
# create a new list consisting of each of the numbers in the first 
# list multiplied by the factor. Print this list.

factor = 3
multiplied = []

for num in nums_list:
    multiplied.append(num * factor)
print(multiplied)

print("-----")

# 8. Reverse a String
# Given a string, print the string reversed.

my_string = "Victoria"

reversed_string = ""
for i in range(len(my_string)-1, -1, -1): 
    # for range function - start: last index in string, 
    # end: at 0 (stop index not included), 
    # step: -1
    reversed_string += my_string[i]
    # print(reversed_string)
print(reversed_string)
