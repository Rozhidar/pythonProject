dog_food_packages = int(input())
cat_food_packages = int(input())

dog_food_price = 2.50
cat_food_price = 4

dog_food_final_price = dog_food_packages * dog_food_price
cat_food_final_price = cat_food_packages * cat_food_price

total = dog_food_final_price + cat_food_final_price

print(f"{total} lv.")