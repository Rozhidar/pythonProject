import sys

biggest_num = -sys.maxsize
sum_of_numbers = 0
current_num = 0
number = int(input())

for num in range(number):
    current_num = int(input())

    if current_num > biggest_num:
        biggest_num = current_num

    sum_of_numbers += current_num

    if biggest_num == sum_of_numbers - biggest_num:
        print('Yes')
        print(f'Sum = {biggest_num}')

    else:
        diff = abs(sum_of_numbers - biggest_num)
        print('No')
        print(f'Diff = {diff}')
