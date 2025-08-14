list_fruits = ['Apple', 'Banana', 'Cherry', 'Apple'] # Modifiable (Mutable)
tuple_fruits = ('Apple', 'Banana', 'Cherry', 'Apple') # Not Modifiable (Immutable)
print(list_fruits)
print(tuple_fruits)
# Indexing
print(list_fruits[0])
print(tuple_fruits[0])
# Negative Indexing
print(list_fruits[-1])
print(tuple_fruits[-1])
# Length Func
print(len(list_fruits))
print(len(tuple_fruits))
# Slicing
print(list_fruits[0:2])
print(tuple_fruits[0:2])
# Replacing
list_fruits[1] = "Pineapple"
print(list_fruits)
# tuple_fruits[1] = "Pineapple" # ERROR
print(tuple_fruits)
list_fruits.append('Watermelon')
print(list_fruits)
list_fruits.remove('Cherry')
print(list_fruits)
print(tuple_fruits)
# tuple_fruits.append('Watermelon') # ERROR
# tuple_fruits.remove('Cherry') # ERROR
print(tuple_fruits.count('Apple')) # Count 'Apple' in tuple_fruits
print(tuple_fruits.index('Apple'))