type_figure = input()

area_result = 0

if type_figure == 'square':
    a = float(input())
    area_result = a * a

elif type_figure == 'rectangle':
    a = float(input())
    b = float(input())
    area_result = a * b

elif type_figure == 'circle':
    r = float(input())
    from math import pi

    area_result = pi * (r ** 2)

elif type_figure == 'triangle':
    b = float(input())
    h = float(input())
    area_result = h * b / 2

print(f'{area_result:.3f}')
