# a = 100
# b = 20
# if a > b:
#     print(f"A is greater")
# else:
#     print(f"B is greater")

# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
# if a > b:
#     print("{} is greater than {}".format(a,b))
# else:
#     print("{} is greater than {}".format(b,a))


a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

if (a > b) and (a > c):
    print("a is greater")
elif (b > a) and (b > c):
    print("b is greater")
else:
    print("c is greater")

'''
SHORTHAND
SAME LINE IF: if a > b: print("a is greater than b")
print("A") if a > b else print("B")
MULTIPLE_CONDITION: print("A") if a > b else print("=") if a == b else print("B")

'''


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")