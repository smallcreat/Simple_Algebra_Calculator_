print('Hi. Welcome to the calculator. Please choose what type of equation you want.')
print('Note: No need to inset a variable because it is unneeded')
print('y + mc = x put 1 for this equation and 4 for y - mc = x.')
print('mc = y + x put 2 for this equation and 5 for mc = y - x.')
print('y = mc + x put 3 for this equation and 6 for y = mc - x.')
a = int(input('What is your number'))
if a == 1:
    print('Please input your numbers')
    y = input('a number which represents y')
    y = float(y)
    x = input('a number which represents x')
    x = float(x)
    m = input('a number of the variable which represents m')
    m = float(m)
    print('c is the variable in the step by step.')
    print('Here is a step by step')
    print(f'First we subtract {y} from {x} and {y} from {y} so we are left with {m} * c and {x} - {y}')
    print(x - y)
    print(y - y)
    print(f'Now we divide {x} and {m} * c by {m}')
    u = ((x - y) / m)
    print(f'Now we have our answer {u}')
elif a == 2:
    y = input('a number which represents y')
    y = float(y)
    x = input('a number which represents x')
    x = float(x)
    m = input('a number of the variable which represents m')
    m = float(m)
    print('c is the variable in the step by step.')
    print('Here is a step by step')
    print(f'First we do {y} + {x}')
    print(y + x)
    print(f'Now we divide {m} * c by {m} and {y} + {x} by {m}')
    u = (y + x) / m
    print(f'So our answer is {u}')
elif a == 3:
    y = input('a number which represents y')
    y = float(y)
    x = input('a number which represents x')
    x = float(x)
    m = input('a number of the variable which represents m')
    m = float(m)
    print('c is the variable in the step by step.')
    print('Here is a step by step')
    print('First we need to have the variables and the numbers on the other side')
    print(f'So now we move mc to the other side and we get {y} - {m} * c = {x}')
    print(f'Now we need to move y to the other side and we get {m} * c and {x} - {y}')
    print(f'{m} * c');
    print(x - y);
    print(f'Now we divide {m} * c by {m} which leaves "c" and {x} - {y} by {m}');
    u = ((x - y) / m);
    print(f'So our answer is {u}');
elif a == 4:
    y = input('a number which represents y')
    y = float(y)
    x = input('a number which represents x')
    x = float(x)
    m = input('a number of the variable which represents m')
    m = float(m)
    print('c is the variable in the step by step.');
    print('Here is a step by step');
    print(f'You need to move {x} to x which out equation will look like this: {m} * c {x} - {y} But the {m} * c supposed to be negative')
    print(x - y);
    u = (x - x - x);
    print(f'Now we need divide both sides by {m} and in {m} * c divided by {m} we just put c')
    print(u / m);
    print(f'So our answer is {u}');
elif a == 5:
    y = input('a number which represents y')
    y = float(y)
    x = input('a number which represents x')
    x = float(x)
    m = input('a number of the variable which represents m')
    m = float(m)
    print('c is the variable in the step by step.');
    print('Here is a step by step')
    print(f'First we do {y} - {x}')
    print(y - x);
    print(f'Now we divide {y} - {x} by {m} so it will be ({y} - {x}) / {m} and we divide {m} * c by {m} so it will be {m} * c / {m}');
    u = ((y - x) / m)
    print(f'So out answer is {u}')
elif a == 6:
    print('Please input your numbers');
    y = input('a number which represents y');
    y = float(y);
    x = input('a number which represents x');
    x = float(x);
    m = input('a number of the variable which represents m');
    m = float(m);
    print('c is the variable in the step by step.');
    print('Here is a step by step');
    print(f'First we need to move {x} to the side of {y} so we have {x} + {y} and {m} * c');
    print(f'Now we have {x} and {y}');
    print(x + y);
    print(f'Now we divide both sides by {m} so we have ({x} + {y}) / {m} and {m} * c / {m}');
    u = ((x + y) / m);
    print(f'So our answer is {u}');
else:
    print('Error, please start again.')

