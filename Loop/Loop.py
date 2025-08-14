# print(range(5, 10))
# for a in range(1, 101, 2):
#     print(a, end=" ")

# for i in range(10):
#     num = input('Enter value: ')
#     print(num)

# numbers = []
# for i in range(10):
#     num = int(input('Enter number: '))
#     numbers.append(num)
#     print(numbers)

# LIST COMPREHENSION

# numbers = [i*i for i in range(100)]
# print(numbers)
# n = int(input('Enter n: '))
# for i in range(n, 0, -2):
#     print(i, end=" ")

# ASCII RANGE (0 - 255)

# for i in range(ord('a'), ord('z')+1):
#     print(i, chr(i))

numbers = []
for i in range(5):
    num = int(input('Enter num: '))
    numbers.append(num)
print(numbers)
# print(len(numbers)) # len() return length of list
for i in range(len(numbers)):
    print(numbers[i])
