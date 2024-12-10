budget = float(input())
season = input()

destination = ''
type_of_vacation = ''
spent_money = 0

if budget <= 100:
    destination = 'Bulgaria'

    if season == 'summer':
        type_of_vacation = 'Camp'
        spent_money = budget * 0.30

    elif season == 'winter':
        type_of_vacation = 'Hotel'
        spent_money = budget * 0.70

elif budget <= 1000:
    destination = 'Balkans'

    if season == 'summer':
        type_of_vacation = 'Camp'
        spent_money = budget * 0.40

    elif season == 'winter':
        type_of_vacation = 'Hotel'
        spent_money = budget * 0.80

elif budget > 1000:
    destination = 'Europe'
    type_of_vacation = 'Hotel'
    spent_money = budget * 0.90

print(f"""Somewhere in {destination} 
{type_of_vacation} - {spent_money:.2f}""")



