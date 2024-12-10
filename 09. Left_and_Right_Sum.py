numbers = int(input())

left_sum = 0
right_sum = 0

for i in range(numbers):
    current = int(input())
    left_sum += current

for i in range(numbers):
    current = int(input())
    right_sum += current

result = 0

if left_sum == right_sum:
    result = left_sum
    print(f'Yes, sum = {result}')

else:
    result = abs(left_sum - right_sum)
    print(f'No, diff = {result}')

