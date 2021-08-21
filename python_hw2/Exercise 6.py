a = int(input('Enter apartment number '))
if 0 < a <= 144:
    print(f'On the {int((a - 1) % 36 / 4 + 1)}th floor')
if 0 < a <= 36:
    print('Entrance 1')
elif 36 < a <= 72:
    print('Entrance 2')
elif 72 < a <= 108:
    print('Entrance 3')
elif 108 < a <= 144:
    print('Entrance 4')
else:
    print('No apartment')