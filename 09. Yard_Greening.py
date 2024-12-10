square_meters_for_greening = float(input())

one_square_meter_price = 7.61

first_price_for_one_square_meter = square_meters_for_greening * one_square_meter_price

discount = first_price_for_one_square_meter * 0.18

final_price = first_price_for_one_square_meter - discount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")