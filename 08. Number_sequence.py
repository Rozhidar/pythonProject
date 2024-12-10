n = int(input())

max_value = 0
min_value = 0

for i in range(n):
    current_number = int(input())
    if i == 0:
        max_value = current_number
        min_value = current_number

    else:

        if current_number > max_value:
            max_value = current_number

        if current_number < min_value:
            min_value = current_number

print(f"""Max number: {max_value}
Min number: {min_value}""")
