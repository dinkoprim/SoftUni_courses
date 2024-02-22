def sorting_cheeses(**kwargs):
    result = ''
    sorted_result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))

    for cheese, qty in sorted_result:
        result += cheese + '\n'
        for num in sorted(qty, reverse=True):
            result += f"{num}\n"

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
