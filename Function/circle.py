def diameter(radius):
    return 2 * radius

def circumference(radius):
    return 2 * 3.1416 * radius

def area(radius):
    return 3.1416 * radius * radius


radius = 10.4
d = diameter(radius)
c = circumference(radius)
a = area(radius)

print("Diameter = {}, Circumference = {}, Area = {}".format(d,c,a))