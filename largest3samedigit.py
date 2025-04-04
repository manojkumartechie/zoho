# Input string
s = "6777133339"

# List of all same 3-digit numbers (111, 222, ..., 999)
same_3_digit_numbers = [str(x) * 3 for x in range(1, 10)]

# Check for presence of each number in the string
found_numbers = [int(num) for num in same_3_digit_numbers if num in s]

# Find the largest same 3-digit number
largest_number = max(found_numbers) if found_numbers else None

print("Largest same 3-digit number:", largest_number)
