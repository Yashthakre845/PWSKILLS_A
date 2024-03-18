# Q1. Create a python program to sort the given list of tuples based on integer value using a lambda function.
input_list = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_list = sorted(input_list, key=lambda x: x[1])
print(sorted_list)

# Q2. Write a Python Program to find the squares of all the numbers in the given list of integers using lambda and map functions.
input_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_numbers = list(map(lambda x: x ** 2, input_numbers))
print(squared_numbers)

# Q3. Write a python program to convert the given list of integers into a tuple of strings. Use map and lambda functions
input_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
converted_tuple = tuple(map(lambda x: str(x), input_integers))
print(converted_tuple)

# Q4. Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25.
from functools import reduce
numbers_list = list(range(1, 26))
product = reduce(lambda x, y: x * y, numbers_list)
print(product)

# Q5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function.
input_numbers = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]
filtered_numbers = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, input_numbers))
print(filtered_numbers)

# Q6. Write a python program to find palindromes in the given list of strings using lambda and filter function.
input_strings = ['python', 'php', 'aba', 'radar', 'level']
palindromes = list(filter(lambda x: x == x[::-1], input_strings))
print(palindromes)
