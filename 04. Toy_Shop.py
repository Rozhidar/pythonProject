excursion_price = float(input())
puzzles_count = int(input())
talking_dolls_count = int(input())
stuffed_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzles_price = 2.60
talking_dolls_price = 3
stuffed_bears_price = 4.10
minions_price = 8.20
trucks_price = 2

all_toys_count = puzzles_count + talking_dolls_count + stuffed_bears_count + minions_count + trucks_count

price_for_all_toys = ((puzzles_count * puzzles_price)
                      + (talking_dolls_count * talking_dolls_price)
                      + (stuffed_bears_count * stuffed_bears_price)
                      + (minions_count * minions_price)
                      + (trucks_count * trucks_price))

discount = 0

if all_toys_count >= 50:
    discount = price_for_all_toys * 0.25
price_for_all_toys = price_for_all_toys - discount

rent_sum = price_for_all_toys * 0.10

money_left = price_for_all_toys - rent_sum

if money_left >= excursion_price:
    money_left = money_left - excursion_price
    print(f"Yes! {money_left:.2f} lv left.")
elif excursion_price > money_left:
    money_needed = excursion_price - money_left
    print(f"Not enough money! {money_needed:.2f} lv needed.")


