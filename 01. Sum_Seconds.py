import math

racer_one = int(input())
racer_two = int(input())
racer_three = int(input())

all_racers_time = racer_one + racer_two + racer_three

convert_time_to_minutes = all_racers_time // 60
convert_to_seconds = all_racers_time % 60

racers_time_in_minutes = math.floor(convert_time_to_minutes)

if convert_to_seconds < 10:
    print(f'{racers_time_in_minutes}:0{convert_to_seconds}')
else:
    print(f'{racers_time_in_minutes}:{convert_to_seconds}')

