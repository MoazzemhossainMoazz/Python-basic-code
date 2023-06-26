# summation values and return sum value
def add(a, b):
    sum = a + b
    return sum

result = add(20, 30)
print("Result = ", result)

# return large value
print("\nFind large number: ")

def large(a, b):
    if a>b:
        return a
    else:
        return b
maximum = large
print(maximum(100, 90))