peters_budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

video_cards_price = video_cards_count * 250

processor_price = video_cards_price * 0.35
ram_memory_price = video_cards_price * 0.10

price_for_products = (video_cards_price + (processor_price * processors_count)
                                             + (ram_memory_price * ram_memory_count))

if video_cards_count > processors_count:
    discount = price_for_products * 0.15
    price_for_products = price_for_products - discount

if peters_budget >= price_for_products:
    left_budget = peters_budget - price_for_products
    print(f"You have {left_budget:.2f} leva left!")

elif peters_budget < price_for_products:
    needed_sum = price_for_products - peters_budget
    print(f"Not enough money! You need {needed_sum:.2f} leva more!")