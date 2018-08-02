# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no
# divisors.). You can(and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions,
# described below.

# Functions
# Reusable functions
# Default arguments

from sympy import isprime

while True:
    x = int(input("Choose a number "))

    if isprime(x) is True:
        print("yes, it is prime")
    else:
        print("no, it is not prime")


# print sympy.isprime(10)
