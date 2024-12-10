flower_type = input()
flower_count = int(input())
budget = int(input())

total_price = 0
discount = 0
raise_of_the_cost = 0

if flower_type == 'Roses':
    roses_price = 5
    total_price = roses_price * flower_count

    if flower_count > 80:
        discount = total_price * 0.10
        total_price = total_price - discount

if flower_type == 'Dahlias':
    dahlias_price = 3.80
    total_price = dahlias_price * flower_count

    if flower_count > 90:
        discount = total_price * 0.15
        total_price = total_price - discount


if flower_type == 'Tulips':
    tulips_price = 2.80
    total_price = tulips_price * flower_count

    if flower_count > 80:
        discount = total_price * 0.15
        total_price = total_price - discount


if flower_type == 'Narcissus':
    narcissus_price = 3
    total_price = narcissus_price * flower_count

    if flower_count < 120:
        raise_of_the_cost = total_price * 0.15
        total_price = total_price + raise_of_the_cost


if flower_type == 'Gladiolus':
    gladiolus_price = 2.50
    total_price = gladiolus_price * flower_count

    if flower_count < 80:
        raise_of_the_cost = total_price * 0.20
        total_price = total_price + raise_of_the_cost

diff = 0

if budget >= total_price:
    diff = budget - total_price
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {diff:.2f} leva left.")

elif budget < total_price:
    diff = total_price - budget
    print(f"Not enough money, you need {diff:.2f} leva more.")











