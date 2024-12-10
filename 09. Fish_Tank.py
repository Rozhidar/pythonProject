length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())
percentage = float(input())

volume_of_fish_tank = length_in_cm * width_in_cm * height_in_cm
volume_in_liters = volume_of_fish_tank / 1000

occupied_space = percentage / 100

needed_liters = volume_in_liters * (1 - occupied_space)

print(needed_liters)
