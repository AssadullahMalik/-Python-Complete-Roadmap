class NegativeNumberError(Exception):
    pass


def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid data type")
    else:
        print("Result:", result)
    finally:
        print("Execution completed")


def check_positive(number):
    if number < 0:
        raise NegativeNumberError("Negative numbers are not allowed")
    return number


# Testing exception handling
divide_numbers(10, 2)
divide_numbers(10, 0)

try:
    check_positive(-5)
except NegativeNumberError as e:
    print("Custom Exception:", e)
