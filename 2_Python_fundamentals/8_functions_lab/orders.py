product = input()
quantity_ordered = int(input())


def total_price_calc(item, quantity):
    prices = {
        'coffee': 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }
    if product in prices:
        item_price = prices[product]
        total_price = quantity_ordered * item_price
        return total_price


print(f'{total_price_calc(product, quantity_ordered):.2f}')