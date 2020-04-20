num_list = range(1,11)
# cubed_nums = []

# how you think you could do it.
# for num in num_list:
#   cubed_nums.append(num ** 3)

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

# This example uses list comprehension in Python. The commented out portions are descriptive of ways that you could do this using normal functions.

#The following develops a dynamic value. 
num_list = range(1,11)
 
# even_numbers = []
# for num in num_list:
#     if num % 2 == 0:
#         even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]

print(list(num_list))
print(even_numbers)

