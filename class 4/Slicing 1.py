# SYNTAX: numbers[start_Index(Inclusive and Optional):end_Index(Exclusive and Optional):step(Optional)]
# Start Index default is 0
# End Index default is lastIndex+1
# Step size default is 1
numbers = [3, 4, 5, 1, 2, 3]
print(numbers[0:3]) # 3, 4, 5
newList = numbers[1:5] # 4 5 1 2
print(newList)
print(numbers[1:6]) # from 1 to 5
print(numbers[1:]) # from 1 to end

print(numbers[0:4]) # from 0 to 3
print(numbers[:4]) # from 0 to 3
print(numbers[:]) # Entire List
print(numbers) # Entire List
print(numbers[0:5:1]) # 3 4 5 1 2
print(numbers[0:5])
print(numbers[0:5:2]) # 3 5 2