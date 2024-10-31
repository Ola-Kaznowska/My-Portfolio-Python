# Getting text from the user
text = input("Enter text: ")

# Definition of vowels (both lowercase and uppercase)
vowels = "aeiouyAEIOUY"

# Initializing counters
vowel_count = 0
consonant_count = 0

# Iterating through each character in the provided text
for char in text:
    if char.isalpha():  # Checking if the character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

# Displaying the results
print("Number of vowels:", vowel_count)

print()

print("Number of consonants:", consonant_count)
