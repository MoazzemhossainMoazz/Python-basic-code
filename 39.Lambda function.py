def calculate(a,b):
    return a*a + 2*a*b + b*b


print(calculate(2,3))

#another way


print((lambda a,b : a*a + 2*a*b + b*b)(2,3))

#another way

a = (lambda a,b : a*a + 2*a*b + b*b)(2,3)
print(a)

#another way

a = (lambda x: x*x*x)(2)
print(a)