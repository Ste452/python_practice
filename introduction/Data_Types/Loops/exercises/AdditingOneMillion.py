"""

# 5 - Exercise Additing One Million

Adding a million: Create a list of numbers from one to one million, and then use min() and max() to ensure your list actually starts at one and ends at one million. 
Additionally, use the sum() function to see how quickly Python can add a million numbers.

"""

numbers = list(range(1, 1000000+1))

print(f"Min: {min(numbers)}")

print(f"Max: {max(numbers)}")

total_sum = sum(numbers)
print(f"Total sum: {total_sum}")