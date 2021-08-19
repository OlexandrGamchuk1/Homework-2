a = float(input('Enter the side of the triangle '))
b = float(input('Enter the side of the triangle '))
c = float(input('Enter the side of the triangle '))
p = (a + b + c) / 2
s = ((p * (p - a) * (p - b) * (p - c))**0.5)
print(f'Area of a triangle {s}')
