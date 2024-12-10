chicken_menus_count = int(input())
fish_menus_count = int(input())
vegetarian_menus_count = int(input())

chicken_menu_price = 10.35
fish_menus_price = 12.40
vegetarian_menus_price = 8.15

ordered_chicken = chicken_menus_count * chicken_menu_price
ordered_fish = fish_menus_count * fish_menus_price
ordered_vegetarian = vegetarian_menus_count * vegetarian_menus_price

total_for_menus = ordered_chicken + ordered_fish + ordered_vegetarian

dessert_price = total_for_menus * 0.20
shipping_price = 2.50

total_price_for_order = total_for_menus + dessert_price + shipping_price

print(total_price_for_order)
