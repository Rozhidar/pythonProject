count_of_pen_packages = int(input())
count_of_marker_packages = int(input())
white_board_cleaner_in_liters = int(input())
percentage_of_discount = int(input())

pen_packages_price = count_of_pen_packages * 5.80
marker_packages_price = count_of_marker_packages * 7.20
white_board_cleaner_price = white_board_cleaner_in_liters * 1.20

price_of_all_materials = pen_packages_price + marker_packages_price + white_board_cleaner_price
discount_calc = price_of_all_materials * (percentage_of_discount / 100)

total_price = price_of_all_materials - discount_calc

print(total_price)