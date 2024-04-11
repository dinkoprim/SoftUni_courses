def calculate_taxes(price):
    tax = 0.20
    return price * tax

def calculate_discount(total_price_with_taxes, customer_type):
    special_discount = 0.10
    regular_discount = 0.00
    if customer_type == "special":
        return total_price_with_taxes * special_discount
    return regular_discount

def main():
    prices = []
    while True:
        price_input = input()
        if price_input == "special" or price_input == "regular":
            customer_type = price_input
            break
        try:
            price = float(price_input)
            if price <= 0:
                print("Invalid price!")
            else:
                prices.append(price)
        except ValueError:
            print("Invalid price!")

    if len(prices) == 0:
        print("Invalid order!")
        return

    total_price_without_taxes = sum(prices)
    total_taxes = sum(calculate_taxes(price) for price in prices)
    total_price_with_taxes = total_price_without_taxes + total_taxes
    discount = calculate_discount(total_price_with_taxes, customer_type)
    final_price = total_price_with_taxes - discount

    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")

if __name__ == "__main__":
    main()