def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as error:
    print("Error:", error)  
