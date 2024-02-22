order = {}

line = input()
while line != 'buy':
    tokens = line.split()
    name, price, qty = tokens[0], float(tokens[1]), int(tokens[2])

    if name not in order.keys():
        order[name] = (price, qty)
    else:
        order[name] = (price, order[name][1] + qty)

    line = input()

[print(f'{k} -> {v[0] * v[1]:.2f}') for k, v in order.items()]
