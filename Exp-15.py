import tracemalloc

class Student:
    def __init__(self, name):
        self.name = name
        self.data = [0] * 1000

tracemalloc.start()

# Memory before creating objects
print("Initial Memory:", tracemalloc.get_traced_memory()[0], "bytes")

# Creating 1st object
s1 = Student("Aditya")
print("After 1st Object:", tracemalloc.get_traced_memory()[0], "bytes")

# Creating 2nd object
s2 = Student("Rahul")
print("After 2nd Object:", tracemalloc.get_traced_memory()[0], "bytes")

# Creating 3rd object
s3 = Student("Amit")
print("After 3rd Object:", tracemalloc.get_traced_memory()[0], "bytes")

tracemalloc.stop()