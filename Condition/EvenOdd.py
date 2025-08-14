def EvenOrOdd(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

num = int(input('Enter a number: '))
result = EvenOrOdd(num)
if result == True:
    print("Even")
else:
    print("Odd")