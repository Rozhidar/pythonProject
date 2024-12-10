exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_in_minutes = exam_hour * 60 + exam_minutes
arrival_time_in_minutes = arrival_hour * 60 + arrival_minutes

diff = exam_time_in_minutes - arrival_time_in_minutes

if diff > 30:
    print('Early')
elif diff < 0:
    print('Late')
else:
    print('On time')

hours = abs(diff) // 60
minutes = abs(diff) % 60

result = ''

if hours > 0:
    result += f'{hours}:{minutes:02d} hours'
elif minutes > 0:
    result += f'{minutes} minutes'


if diff > 0:
    result += ' before the start'
elif diff < 0:
    result += ' after the start'

print(result)



