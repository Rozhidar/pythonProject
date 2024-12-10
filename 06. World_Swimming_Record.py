import math

record_in_seconds = float(input())
distance_in_meters = float(input())
one_meter_swum_in_sec = float(input())

calc_for_time = distance_in_meters * one_meter_swum_in_sec

slowdown_in_every_fifteen_meters = math.floor(distance_in_meters / 15)
slowdown = slowdown_in_every_fifteen_meters * 12.5

total_time = calc_for_time + slowdown

if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

elif total_time >= record_in_seconds:
    difference = total_time - record_in_seconds
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
