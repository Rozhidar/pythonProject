movie_budget = float(input())
extras_count = int(input())
price_for_clothes_for_one_extra = float(input())

decor_sum = movie_budget * 0.10

clothes_sum = extras_count * price_for_clothes_for_one_extra

clothes_sum_after_discount = 0

if extras_count > 150:
    discount = clothes_sum * 0.10
    clothes_sum_after_discount = clothes_sum - discount
else:
    clothes_sum_after_discount = clothes_sum

total_price_for_movie = decor_sum + clothes_sum_after_discount

if total_price_for_movie > movie_budget:
    calc_difference = total_price_for_movie - movie_budget
    print(f"Not enough money!")
    print(f"Wingard needs {calc_difference:.2f} leva more.")
elif total_price_for_movie <= movie_budget:
    calc_difference = movie_budget - total_price_for_movie
    print("Action!")
    print(f"Wingard starts filming with {calc_difference:.2f} leva left.")
