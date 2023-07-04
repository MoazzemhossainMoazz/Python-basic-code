num = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*x,num))
print(result)

# [expression for item in list]

result = [x*x for x in num]
print(result)

#find even number from list use filter function
print("\nfind even number from list use filter function")
result = list(filter(lambda x : x%2==0, num))
print(result)

#another way
print("another way")
result = [x for x in num if x%2==0]
print(result)
