days_of_stay = int(input())
type_accommodation = input()
valuation = input()

night_price = 0
price = 0
discount = 0

if type_accommodation == 'room for one person':
    night_price = 18

    if days_of_stay < 10:
        price = (days_of_stay - 1) * night_price

    elif 10 <= days_of_stay <= 15:
        price = (days_of_stay - 1) * night_price

    elif days_of_stay > 15:
        price = (days_of_stay - 1) * night_price

elif type_accommodation == 'apartment':
    night_price = 25

    if days_of_stay < 10:
        price = (days_of_stay - 1) * night_price
        discount = price * 0.30
        price = price - discount

    elif 10 <= days_of_stay <= 15:
        price = (days_of_stay -1) * night_price
        discount = price * 0.35
        price = price - discount

    elif days_of_stay > 15:
        price = (days_of_stay -1) * night_price
        discount = price * 0.50
        price = price - discount

elif type_accommodation == 'president apartment':
    night_price = 35

    if days_of_stay < 10:
        price = (days_of_stay - 1) * night_price
        discount = price * 0.10
        price = price - discount

    elif 10 <= days_of_stay <= 15:
        price = (days_of_stay -1) * night_price
        discount = price * 0.15
        price = price - discount

    elif days_of_stay > 15:
        price = (days_of_stay -1) * night_price
        discount = price * 0.20
        price = price - discount

if valuation == 'positive':
    additional_money = price * 0.25
    price = price + additional_money

elif valuation == 'negative':
    deducted_money = price * 0.10
    price = price - deducted_money

print(f'{price:.2f}')