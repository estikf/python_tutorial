# Functions
"""
def sum_without_args(num1=5,num2=0):
    return num1 + num2

print(sum_without_args(3,1))"""    # Invoke a function

# *args ve **kwargs

"""def sum_with_args(*nums):
    result = 0
    
    for i in nums:
        result += i
    
    print(type(nums))
    print(result)


def sum_with_kwargs(name="Furkan",surname="Estik"):
    
    print(name)
    print(surname)

sum_with_kwargs()
        """

# List / Dictionary / Tuple / Set as an Argument

"""
my_dict =  {
    "Employee_name":"John",
    "Employee_surname":"Doe",
    "Employee_features":
        {
            "salary":10000,
            "is_car_exists":True
        }

}
    
def list_operations(dictionary,maas):

    dictionary["Employee_features"]["salary"] = maas
    print(dictionary["Employee_features"]["salary"])


list_operations(my_dict,4000)

my_dict["Employee_features"]["salary"]"""

# Recursion (Fibonacci Ödev)

"""def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(6))"""

# Decorators

def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Something is happening before the function is called.")
        func(*args,**kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee(*args,**kwargs):
    
    print(args)
    print(kwargs)

say_whee("Example",name="Example")

# Lambda

"""def myfunc(n):
  return lambda a : a * n

my_doubler = myfunc(3)

my_result = my_doubler(15)

print(my_result)
"""

# Filter

my_list = [x for x in range(10)]

a = filter(lambda x: x>3, my_list)

yeni_list = []

print(type(a))

for i in a:
    yeni_list.append(i)

print(yeni_list)

# Map

def my_sum(n):
    if n==0:
        return "Ben sıfırım"
    elif n>3 and n<7:
        return n*2
    else:
        return n

result = map(my_sum, my_list)

print(set(result))

