type_of_film_show = input()
rows = int(input())
columns = int(input())

count_of_seats = rows * columns
price_of_all_seats = 0

if type_of_film_show == 'Premiere':
    price_of_all_seats = count_of_seats * 12.00
elif type_of_film_show == 'Normal':
    price_of_all_seats = count_of_seats * 7.50
elif type_of_film_show == 'Discount':
    price_of_all_seats = count_of_seats * 5.00

print(f'{price_of_all_seats:.2f} leva')
