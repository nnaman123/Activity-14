#find factorial of a number using recursive function
def factorial(x):
    """This is a recursive function to find the factorial of an integer"""

    if x==0 or x==1:
            return 1
    else:
            return (x*factorial(x-1))

#display the output
print(factorial.__doc__)
print("The factorial of 1 is",factorial(1))
print("The factorial of 3 is",factorial(3))
print("The factorial of 5 is",factorial(5))
print("The factorial of 7 is",factorial(7))
print("The factorial of 10 is",factorial(10))
