
# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.
def odd_numbers():
    return [num for num in range(1, 26) if num % 2 != 0]
print(odd_numbers())


# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs to demonstrate their use.
def args_function(*args):
    for arg in args:
        print(arg)

def kwargs_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].
# An iterator is an object that allows iteration over a sequence. The method used to initialize the iterator object is iter() and the method used for iteration is next().
num_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
iterator_obj = iter(num_list)
for _ in range(5):
    print(next(iterator_obj))

# Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function.
# A generator function is a function that returns an iterator called a generator. The yield keyword is used to return data from a generator function without destroying the state of the function.
def countdown(num):
    while num > 0:
        yield num
        num -= 1

# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.
def prime_generator():
    num = 2
    prime_count = 0
    while prime_count < 20:
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            yield num
            prime_count += 1
        num += 1

prime_gen = prime_generator()
for _ in range(20):
    print(next(prime_gen))

# Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.
a, b = 0, 1
count = 0
while count < 10:
    print(a)
    a, b = b, a + b
    count += 1

# Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
# Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']
string = 'pwskills'
output_list = [char for char in string]
print(output_list)

# Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.
def is_palindrome(num):
    original_num = num
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10
    return original_num == reverse_num

# Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
odd_numbers = [num for num in range(1, 101) if num % 2 != 0]
print(odd_numbers)
