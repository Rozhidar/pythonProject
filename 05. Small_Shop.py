product = input()
city = input()
quantity = float(input())

price_calc = 0

if city == 'Sofia':

    if product == 'coffee':
        price_calc = quantity * 0.50

    elif product == 'water':
        price_calc = quantity * 0.80

    elif product == 'beer':
        price_calc = quantity * 1.20

    elif product == 'sweets':
        price_calc = quantity * 1.45

    elif product == 'peanuts':
        price_calc = quantity * 1.60

elif city == 'Plovdiv':

    if product == 'coffee':
        price_calc = quantity * 0.40

    elif product == 'water':
        price_calc = quantity * 0.70

    elif product == 'beer':
        price_calc = quantity * 1.15

    elif product == 'sweets':
        price_calc = quantity * 1.30

    elif product == 'peanuts':
        price_calc = quantity * 1.50

elif city == 'Varna':

    if product == 'coffee':
        price_calc = quantity * 0.45

    elif product == 'water':
        price_calc = quantity * 0.70

    elif product == 'beer':
        price_calc = quantity * 1.10

    elif product == 'sweets':
        price_calc = quantity * 1.35

    elif product == 'peanuts':
        price_calc = quantity * 1.55

print(price_calc)