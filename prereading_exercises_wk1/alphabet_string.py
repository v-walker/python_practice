alphabet = "abcdefghijklmnopqrstuvwxyz"

print("The first letter is", alphabet[0])

print("The first three letters are", alphabet[:3])

print("Some letters in the middle are", alphabet[11:16])

print(f"There are {len(alphabet)} letters in the alphabet")

for letter in alphabet:
    print(letter)

alphalist = list(alphabet)
alphalist[0] = "4"

print(alphalist)

alphabet = "".join(alphalist)
print(alphabet)