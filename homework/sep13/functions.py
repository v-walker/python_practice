# Homework
# Functions

# 1. Find the smallest number
# Write a function smallest that accepts a List of numbers as an argument.
# It should return the smallest number in the List.

def smallest_num(nums):
    i = 0
    for num in nums:
        if num < i:
            i = num
    return i

result = smallest_num([1, -1, 3, 4, -7])
print(result)

# 2. Find the largest number
# Write a function largest that accepts a List of numbers as an argument.
# It should return the largest number in the List.

def largest_num(nums):
    i = 0
    for num in nums:
        if num > i:
            i = num
    return i

result = largest_num([1, -1, 3, 4, -7])
print(result)

# 3. Find the shortest String
# Write a function shortest that accepts a List of Strings as an argument.
# It should return the shortest String in the List.

def shortest_string(strings):
    shortest = strings[0]
    for string in strings:
        if len(string) < len(shortest):
            shortest = string
    return shortest

result = shortest_string(["Hello", "Welcome", "H", "Hi"])
print(result)

# 4. Find the longest String
# Write a function longest that accepts a List of Strings as an argument.
# It should return the longest String in the List.

def longest_string(strings):
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

result = longest_string(["Hello", "Welcome", "H", "Hi"])
print(result)
