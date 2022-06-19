def add(a, b):
    answer = a + b
    return answer

def subtract(a, b):
    answer = a - b
    return answer

def multiply(a, b):
    answer = (a * b)
    return answer

def divide(a, b):
    answer = a / b
    return answer

def modulus(a, b):
    answer = a % b
    return answer

def exponent(a, b):
    answer = a ** b
    return answer

def int_divide(a, b):
    answer = a // b
    return answer

def square(a):
    answer = a * a
    return answer

def cube(a):
    answer = a * a * a
    return answer

def factorial(a):
    factor = 1
    for num in range(1, a + 1):
        factor *= num
        return factor

