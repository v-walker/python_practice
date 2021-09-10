# Sequences Lab 9/9/21

# 1. Create a new list called "planets" that holds all of 
# the names of the planets in our solar system. Print the 
# list of planets on the command line.

planets = ["Earth", "Jupiter", "Neptune", "Mars", "Saturn", "Mercury", "Uranus", "Venus"]
print(planets)

print("-----")

# 2. Print out how many elements are in the planet list

print(f"There are {len(planets)} planets in our solar system.")

print("-----")

# 3. Create a while loop that iterates through each of the items 
# in the planet list and changes them to lowercase .

i = 0
while i < len(planets):
    print(planets[i].lower())
    i += 1

print("-----")

# 4. Add Pluto to the planet list.

planets.append("Pluto")
print(planets)

print("-----")

# 5. Combine the following 2 lists into a list called Houston.
# Find how many cities are listed in the Houston list
# Add more cities to the Houston list.
# Print the list cities (one city per line)

HoustonCities = ["Katy", "Memorial City", "Sugar Land", "The Heights", "River Oaks", "Pasadena"]
ClearLakeCities = ["League City", "Kemah", "Seabrook", "Webster", "El Lago"]

# combine cities lists to make new list named "Houston"
Houston = HoustonCities + ClearLakeCities
# Add more cities to the Houston list.
Houston.extend(["Conroe", "Baytown"])

# Find how many cities are listed in the Houston list
print(f"We have {len(Houston)} cities in our Houston list.")

# while loop to print list of cities (one city per line)
index = 0
while index < len(Houston):
    print(Houston[index])
    index += 1

print("-----")

# # 6. Since Pluto isn't really a planet, delete it from the planet list

# planets.pop()
# print(planets)

del planets[-1]
# popped_planet = planets.pop() <-- does same as previous statement
print(planets)

print("-----")

# 7. Create the following lists that are a subset of the Houston list:
# htx1 = The first 4 cities
# htx2 = Cities 3-6
# htx3 = The last 2 cities

htx1 = Houston[:4]
print(htx1)

htx2 = Houston[2:6]
print(htx2)

htx3 = Houston[-2:]
print(htx3)

print("-----")

# 8. Insert Denver in the Houston list after The Heights

Houston.insert(4, "Denver")
print(Houston)

print("-----")

# 9. Remove the last city from the Houston List

last_city = Houston.pop()
print(Houston)

print("-----")

# 10. Get the index of Seabrook from the Houston list

print(Houston.index("Seabrook"))

print("-----")

# 11. Sort the list of cities

Houston.sort()
print(Houston)

print("-----")

# # 12. Copy the Houston list to a list called USCities

USCities = Houston.copy()
print(USCities)

print("-----")

# 13. Remove all items from the Houston list

Houston.clear()
print(Houston)

print("-----")

# # 14. Take the following list and multiply 5 times
# nums = [4, 5, 7, 8]

# nums_times_5 = []
# index = 0
# while index < len(nums):
#     nums_times_5.append(nums[index] * 5)
#     index += 1
# print(nums_times_5)

# # 15. Reverse the String "DigitalCrafts"

# my_string = "DigitalCrafts"
# dc_list = list(my_string)
# print(dc_list)
# dc_list_rev = []

# for letter in range(len(dc_list) - 1, -1, -1):
#     dc_list_rev += dc_list[letter]
# print(dc_list_rev)

# reversed_string = "".join(dc_list_rev)
# print(reversed_string)


# # 16. Crete a range
# # [0, 1, 2, 3, 4, 5]

# num_list = []
# index = 0

# while index < 6:
#     num_list.append(index)
#     index += 1
# print(num_list)

# # 17. Create a range
# # [6, 8, 10, 12, 14, 16]

# num_list2 = list(range(6, 17, 2))
# print(num_list2)

# # 18. Loop through the planet list using a for loop and print the name 
# # of each planet

# for planet in planets:
#     print(planet)

# # 19. Loop through the USCities list and print the name of each city

# for city in USCities:
#     print(city)

# # 20. Loop through the following sequence
# nums = [6, 8, 10, 12, 14, 16] 
# # multiply each number by 5.
# # print the result.

# for num in nums:
#     print(num * 5)

# # 21. Create a multiplication table for 1-10
# # i.e. 1x1 = 1 1x2 = 2 1x3 = 3