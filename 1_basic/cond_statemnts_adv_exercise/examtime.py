hour_of_start = int(input())
minute_of_start = int(input())
hour_arrived = int(input())
minute_arrived = int(input())

time_arrived = hour_arrived * 60 + minute_arrived  # in minutes
time_start = hour_of_start * 60 + minute_of_start  # in minutes
diff = abs(time_start - time_arrived)
status = ''
result = ''

if time_start - 30 <= time_arrived <= time_start:
    status = 'On time'
elif time_arrived < time_start - 30:
    status = 'Early'
elif time_arrived > time_start:
    status = 'Late'

hours = diff // 60
minutes = diff % 60

if time_arrived < time_start and diff < 60:
    result = f'{diff} minutes before the start'
elif time_arrived < time_start and diff >= 60:
    if minutes < 10:
        result = f'{hours}:0{minutes} hours before the start'
    elif minutes > 10:
        result = f'{hours}:{minutes} hours before the start'
elif time_arrived > time_start and diff < 60:
    result = f'{diff} minutes after the start'
elif time_arrived > time_start and diff >= 60:
    if minutes < 10:
        result = f'{hours}:0{minutes} hours after the start'
    elif minutes > 10:
        result = f'{hours}:{minutes} hours after the start'

print(status)
print(result)


