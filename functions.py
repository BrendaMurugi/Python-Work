def hello(name, age):
    year = 2022 - age

    print(f"Hello {name}, you were born in {year}.")

hello("Bree", 22)

def my_country(country = "Uganda", student = "Susan"):
    return f"Hello {student} you are from {country}."

def greet_multiple(*names):
    for name in names:
        print(f"Hello {name}.")

#Write a function that accepts any number of integers and returns the sum of all of them.

def sum(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

def multiply(*nums):
    ans = 1
    for num in nums:
        ans *= num
    return ans

def greet_multiple_data(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

greet_multiple_data(name = "Mima", country = "Yemen", age = 19)

def intro(**kwargs):
    keys = kwargs.keys()
    if "country" in keys:
        year = 2022 - kwargs['age']
        print(f"Hello {kwargs['name']} you are from {kwargs['country']} and you were born in {year}.") 
    elif "age" in keys:
        year = 2022 - kwargs['age']
        print(f"Hello {kwargs['name']} you were born in {year}.")
    elif not kwargs:
        print(f"Hello anonymous.")

intro(name = "Mima", country = "Yemen", age = 19)

def sum_and_greet(*args, **kwargs):
    sum = 0
    for num in args:
     sum += num

    keys = kwargs.keys()  
    if "name" in keys:
        print(f"Hello {kwargs['name']}, the answer is {sum}.")

    elif "country" in keys:
        print(f"Hello {kwargs['country']}, the answer is {sum}.")

    elif not kwargs:
        print(f"Hello anonymous, the answer is {sum}.")

sum_and_greet(1,2,3)
