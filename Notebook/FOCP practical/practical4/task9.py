def multiply(a, b=None):
    """
    Multiply two numeric values and return the result.

    If the second argument is not provided, the first argument is
    multiplied by itself.
    """
    if b is None:
        return a * a
    else:
        return a * b

# Testing the function

# Single argument, so it multiplies the value by itself
print(multiply(5))        # Output: 25

# Two arguments, normal multiplication
print(multiply(4, 3))     # Output: 12

# Using keyword arguments (order does not matter)
print(multiply(b=10, a=7))  # Output: 70

# Another single argument test
print(multiply(8))        # Output: 64

# Two arguments using keyword for only one
print(multiply(a=6, b=2)) # Output: 12
