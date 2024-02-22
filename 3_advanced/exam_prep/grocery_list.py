def shop_from_grocery_list(budget, grocery_list, *product_price_pairs):
    for pair in product_price_pairs:
        product = pair[0]
        price = pair[1]
        if product in grocery_list:
            if budget >= price:
                budget -= price
                grocery_list.remove(product)
            else:
                break
    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

