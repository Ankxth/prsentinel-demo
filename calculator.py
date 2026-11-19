"""A small calculator: the four basic operations, plus a reader for "12 / 4"."""

import sys


def add(a, b):
    """Return a + b."""
    return a + b


def multiply(a, b):
    """Return a * b."""
    return a * b


def power(a, b):
    """Return a raised to the power b."""
    return a ** b


def divide(a, b):
    """Return a / b.

    Dividing by zero raises ValueError("Cannot divide by zero").
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(operator, a, b):
    """Apply one operator ("+", "-", "*", "/" or "^") to a and b.

    An operator that is not one of those raises ValueError.
    """
    if operator == "+":
        return add(a, b)
    if operator == "-":
        return subtract(a, b)
    if operator == "*":
        return multiply(a, b)
    if operator == "/":
        return divide(a, b)
    if operator == "^":
        return power(a, b)
    raise ValueError("Unknown operator: %s" % operator)


def evaluate(expression):
    """Work out text of the form "number operator number", e.g. "12 / 4".

    The three parts are separated by spaces and the answer is a float
    ("12 / 4" gives 3.0). Anything else raises ValueError.
    """
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError("Expected: number operator number, e.g. 2 + 3")
    left, operator, right = parts
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("Not a number in: %s" % expression)
    return calculate(operator, a, b)


def main(argv):
    """Command line: python calculator.py "12 / 4" prints 3.0."""
    if len(argv) != 2:
        print('Usage: python calculator.py "12 / 4"')
        return 1
    try:
        print(evaluate(argv[1]))
    except ValueError as err:
        print("Error: %s" % err)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
