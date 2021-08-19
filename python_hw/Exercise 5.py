number = int(input('Enter the digits of the three-digit number '))
a = number // 100
b = number // 10 % 10
c = number % 10
print(f'Sum of three-digit digits {a + b + c}')
