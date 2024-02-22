# input
hour = int(input())
day = str(input())
result = 0
# logic
if 10 <= hour <= 18 and day != 'Sunday':
    result = 'open'
else:
    result = 'closed'
# output
print(result)
