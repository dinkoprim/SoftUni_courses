from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]


def attempt_challenge(tool, substance):
    attempt = tool * substance
    if attempt in challenges:
        challenges.remove(attempt)
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance > 0:
            substances.append(substance)


while substances and tools:
    tool, substance = tools.popleft(), substances.pop()
    attempt_challenge(tool, substance)
    if not challenges:
        print(f"Harry found an ostracon, which is dated to the 6th century BCE.")
        break

if challenges:
    print(f"Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f'Tools: {", ".join(str(x) for x in tools)}')
if substances:
    print(f'Substances: {", ".join(str(x) for x in substances)}')
if challenges:
    print(f'Challenges: {", ".join(str(x) for x in challenges)}')
