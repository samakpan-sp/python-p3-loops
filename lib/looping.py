#!/usr/bin/env python3

def happy_new_year():
    x = 10
    # code goes here!
    while x > 0:
        print(x)
        x -=1
    print("Happy New Year!")
happy_new_year()
pass


def square_integers(int_list):
    squared_list = []  # Create an empty list to store squared elements
    for x in int_list:
        squared_list.append(x**2)  # Square each element and append to the list
    return squared_list  # Return the list of squared elements

# Example usage:
result = square_integers([1, 2, 3, 4, 5])
print(result)  # This will print [1, 4, 9, 16, 25]


# FizzBuzz
def fizzbuzz():
   for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    # code goes here!
print(fizzbuzz())
pass
