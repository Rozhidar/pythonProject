nylon_needed_in_square_meters = int(input())
paint_needed_in_liters = int(input())
thinner_in_liters = int(input())
hours_needed = int(input())

paint_price = 14.50
nylon_price = 1.50
thinner_price = 5.00

additional_ten_percent_of_paint = paint_needed_in_liters + (paint_needed_in_liters * 0.10)
paint_in_total = additional_ten_percent_of_paint * paint_price

additional_two_square_meters_of_nylon = nylon_needed_in_square_meters + 2
nylon_in_total = additional_two_square_meters_of_nylon * nylon_price

thinner_in_total = thinner_in_liters * thinner_price

plastic_bags = 0.40

final_price_for_all_materials = paint_in_total + nylon_in_total + thinner_in_total + plastic_bags

workers_price_calc = final_price_for_all_materials * 0.30
workers_price_in_total = workers_price_calc * hours_needed

sum_in_total = workers_price_in_total + final_price_for_all_materials

print(sum_in_total)
