def grocery_store(**kwargs):
    result = {}
    for product, qty in sorted(kwargs.items(), key=lambda x: (x[1], -len(x[0]), x[0])):
        result[product] = qty

    return '\n'.join(f'{k}: {v}' for k, v in result.items())


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
