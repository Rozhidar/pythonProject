import math

serial_movie_name = input()
duration_of_episode = int(input())
break_duration = int(input())

time_for_lunch = break_duration * 1/8
rest_time = break_duration * 1/4

left_time = break_duration - time_for_lunch - rest_time

if duration_of_episode <= left_time:
    difference = left_time - duration_of_episode
    print(f"You have enough time to watch {serial_movie_name} and left with {math.ceil(difference)} minutes free time.")
elif duration_of_episode > left_time:
    needed_time = duration_of_episode - left_time
    print(f"You don't have enough time to watch {serial_movie_name}, you need {math.ceil(needed_time)} more minutes.")
