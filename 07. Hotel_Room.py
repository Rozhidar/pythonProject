month = input()
night_stays = int(input())

studio_price = 0
apartment_price = 0
studio_discount = 0
apartment_discount = 0
final_price_studio = 0
final_price_apartment = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65

    if 7 < night_stays < 14:
        studio_discount = studio_price * 0.05
        studio_price = studio_price - studio_discount

    elif night_stays > 14:
        studio_discount = studio_price * 0.30
        studio_price = studio_price - studio_discount

        apartment_discount = apartment_price * 0.10
        apartment_price = apartment_price - apartment_discount

elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70

    if night_stays > 14:
        studio_discount = studio_price * 0.20
        studio_price = studio_price - studio_discount

        apartment_discount = apartment_price * 0.10
        apartment_price = apartment_price - apartment_discount

elif month == 'July' or month == 'August':
    studio_price = 76
    apartment_price = 77

    if night_stays > 14:
        apartment_discount = apartment_price * 0.10
        apartment_price = apartment_price - apartment_discount

final_price_apartment = apartment_price * night_stays
final_price_studio = studio_price * night_stays

print(f"""Apartment: {final_price_apartment:.2f} lv.
Studio: {final_price_studio:.2f} lv.""")
