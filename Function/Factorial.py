def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

for i in range(1, 51):
    result = factorial(i)
    print("{}! = {}".format(i, result))