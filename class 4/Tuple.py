information = () # Empty Tuple
print(information)
print(type(information)) # Tuple

my_info = ('Maruf Hossain', 170626, 'Khulna')
print(my_info)
print(my_info[0])
print(my_info[1])
print(my_info[2])
# print(my_info[3]) # ERROR
print(my_info[0:2])
print(my_info[-1])
print(my_info[::-1])

# That's why tuple is immutable

info = ['Maruf Hossain', 170626, 'Khulna']
print(info)
info.append('Dhaka')
print(info)

# List is mutable