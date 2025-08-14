# Taking input
# num1, num2 = input('Enter two integer numbers: ').split()
# sum = num1 + num2;
# print(sum)
# print(type(sum))

result = list(map(int,input('Enter two integer numbers: ').split()))
print(result)