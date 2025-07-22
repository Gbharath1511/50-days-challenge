# Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Check a single number
number = int(input("Enter a number to check: "))
print(f"{number} is {check_even_odd(number)}")

# Now check a list of numbers
number_list = [12, 7, 4, 19, 22, 35]

print("\nChecking list of numbers:")
for num in number_list:
    result = check_even_odd(num)
    print(f"{num} is {result}")
