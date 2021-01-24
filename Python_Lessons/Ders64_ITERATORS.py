class MyEvenNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.start > self.end:
            raise StopIteration
    
        else:
            current = self.start

        if (current %2 != 0):
            self.start += 1
            return next(self)
        
        else:
            self.start +=2
            return current

numbers = MyEvenNumbers(2, 11)


print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))



