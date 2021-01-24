# Examples for recursive functions

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def fibonacci(step):
    step_now = 1
    start_array = [0,1]
    x = 0
    y = 1
    while step_now <= step:
        start_array.append(start_array[x]+start_array[y])
        x += 1
        y += 1
        step_now += 1
    return start_array

def fibonacci_recursion(step):
    
        if step == 0:
            return 0
        elif step == 1:
            return 1
        else:
            return (fibonacci_recursion(step-1) + fibonacci_recursion(step-2))
    

print(fibonacci(10))

    