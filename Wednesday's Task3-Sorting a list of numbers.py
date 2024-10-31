# Initialize an empty list to store numbers
numbers = [] # list

# Loop to get five separate numbers from the user
print("Please enter five numbers:")
for i in range(5): # loop 5 x
    # Prompt the user for each number
    number = input(f"Enter number {i + 1}: ")
    
    # Convert the input to a floating-point number and add it to the list
    number = float(number) # number float
    numbers.append(number) # add the number

# Sort the list of numbers in ascending order
sorted_numbers = sorted(numbers)

# Display each step for clarity
print("Original list of numbers:", numbers)

print()

print("Sorted list of numbers:", sorted_numbers)
