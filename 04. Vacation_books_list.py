count_of_pages = int(input())
pages_read_one_hour = int(input())
count_of_days = int(input())

hours_needed_for_current_book = count_of_pages / pages_read_one_hour
hours_needed_per_day = hours_needed_for_current_book / count_of_days

print(round(hours_needed_per_day))
