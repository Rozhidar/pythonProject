budget_of_the_group = int(input())
season = input()
fisherman_count = int(input())

price_of_the_ship = 0

if season == 'Spring':
    price_of_the_ship = 3000

elif season == 'Summer' or season == 'Autumn':
    price_of_the_ship = 4200

elif season == 'Winter':
    price_of_the_ship = 2600

discount = 0

if fisherman_count <= 6:
    discount = price_of_the_ship * 0.10
    price_of_the_ship = price_of_the_ship - discount

elif 7 <= fisherman_count <= 11:
    discount = price_of_the_ship * 0.15
    price_of_the_ship = price_of_the_ship - discount

elif fisherman_count >= 12:
    discount = price_of_the_ship * 0.25
    price_of_the_ship = price_of_the_ship - discount


if fisherman_count % 2 == 0 and not season == 'Autumn':
    additional_discount = price_of_the_ship * 0.05
    price_of_the_ship = price_of_the_ship - additional_discount

diff = 0

if budget_of_the_group >= price_of_the_ship:
    diff = budget_of_the_group - price_of_the_ship
    print(f"Yes! You have {diff:.2f} leva left.")

elif budget_of_the_group < price_of_the_ship:
    diff = price_of_the_ship - budget_of_the_group
    print(f"Not enough money! You need {diff:.2f} leva.")