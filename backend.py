import math
#Do not make any other imports i.e DO NOT import re

def add(a, b):
    """
    Add two numbers and return the result.
    """
    return a + b

pass

def subtract(a, b):
    """
    Subtract the second number from the first and return the result.
    """
    return b - a
pass

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    """
    return a * b

pass

def divide(a, b):
    """
    Divide the first number by the second and return the result.
    Handle division by zero by returning "Error: Division by zero".
    """
    try:
        return a / b 
    except:
        ZeroDivisionError
        return "Error: Division by zero"


pass

def sqrt(a):
    """
    Return the square root of a number.
    Handle negative inputs by returning "Error: Negative input".
    """
    if a < 0:
        return "Error: Negative input"
    return math.sqrt(a)

pass

def modulus(a, b):
    """
    Return the remainder of the division of the first number by the second.
    Handle division by zero by returning "Error: Division by zero".
    """
    try:
        return a % b
    except:
        ZeroDivisionError
        return "Error: Division by zero"
pass

def exponent(a, b):
    """
    Return the result of raising the first number to the power of the second.
    """
    return a ** b
pass

def factorial(a):
    """
    Return the factorial of a number.
    Handle negative inputs by returning "Error: Negative input".
    """
    if a < 0:
        return "Error: Negative input"
    return math.factorial(a)
pass

def log(a, base):
    """
    Return the logarithm of a number with a specified base.
    Handle invalid inputs by returning "Error: Invalid input".
    """
    try:
        if a <= 0 or base <= 0 or base == 1:
            return "Error: Invalid input"
        return math.log(a, base)
    except ValueError:
        return "Error: Invalid input"

pass

def sin(a):
    """
    Return the sine of a number (in radians).
    """
    return math.sin(a)

pass

def cos(a):
    """
    Return the cosine of a number (in radians).
    """
    return math.cos(a)
pass

def tan(a):
    """
    Return the tangent of a number (in radians).
    Handle undefined cases by returning "Error: Undefined".
    """
    try:
        return math.tan(a)
    except ValueError:
        return "Error: Undefined"
pass

def degrees_to_radians(degrees):
    """
    Convert degrees to radians.
    """
    return math.radians(degrees)
pass

def radians_to_degrees(radians):
    """
    Convert radians to degrees.
    """
    return math.degrees(radians)
pass

def evaluate_expression(expression):
    """
    Evaluate a mathematical expression using PEMDAS/BODMAS rules.
    The expression is a string, e.g., "3 / 7 * 8 % 3".
    This function will call other calculator functions in the correct order.
    DO NOT USE THE eval() expression.
    """
pass
