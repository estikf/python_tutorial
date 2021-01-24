# A Simple Decorator

"""def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Something is happening before the function is called.")
        func(*args,**kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee(*args,**kwargs):
    
    print(args)
    print(kwargs)

say_whee(1,2,3)"""

# A Real World Example

import time

def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i for i in range(10000)])

@timer
def another_function():
    for i in range(0,10000,100):
        print(i)

another_function()