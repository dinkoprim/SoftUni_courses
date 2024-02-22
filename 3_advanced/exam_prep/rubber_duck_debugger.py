from collections import deque

time_values = deque(int(x) for x in input().split())
task_values = deque(int(x) for x in input().split())

roster = {'Darth Vader Ducky':	range(0, 61),
          'Thor Ducky':	range(61, 121),
          'Big Blue Rubber Ducky': range(121, 181),
          'Small Yellow Rubber Ducky': range(181, 241),
          }

result = {'Darth Vader Ducky':	0,
          'Thor Ducky':	0,
          'Big Blue Rubber Ducky': 0,
          'Small Yellow Rubber Ducky': 0,
          }

while time_values and task_values:
    time = time_values.popleft()
    task = task_values.pop()

    attempt = time * task

    for given_ranges in roster.values():
        if attempt in given_ranges:
            for duck, time_range in roster.items():
                if attempt in time_range:
                    result[duck] += 1
                    break
            break

    else:
        task -= 2
        task_values.append(task)
        time_values.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
[print(f'{k}: {v}') for k, v in result.items()]
