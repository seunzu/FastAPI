"""
Functions
"""

# 1
print("Hello and welcome to function")

def my_function():
    print("Inside my_function")

my_function()

# 2
def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

print_my_name("Steve", "Jobs")

# 3
def print_color_red():
    color = "Red"
    print(color)

color = "Blue"
print(color)
print_color_red()

# 4
def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

print_numbers(3, 10)
print_numbers(lowest_number=3, highest_number=10)

# 5
def multiply_numbers(a, b):
    return a * b

solution = multiply_numbers(10, 6)
print(solution)

# 6
def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)

number_list = [1, 2, 3, 4, 5]
print_list(number_list)

# 7
def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate

final_cost = buy_item(50)
print(final_cost)














