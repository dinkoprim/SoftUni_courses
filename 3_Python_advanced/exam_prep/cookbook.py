def cookbook(*args):
    log = {}
    recipe_book = {}

    for recipe, country, ingredients in args:
        if country not in log.keys():
            log[country] = []
        if recipe not in recipe_book.keys():
            log[country].append(recipe)
            recipe_book[recipe] = ingredients

    for cuisine, recipies in log.items():
        log[cuisine] = list(sorted(recipies))

    log = dict(sorted(log.items(), key=lambda x: (-len(x[1]), x[0])))
    result = ''

    for cuisine, recipies in log.items():
        result += f'{cuisine} cuisine contains {len(recipies)} recipes:\n'
        for dish in recipies:
            result += f"  * {dish} -> Ingredients: {', '.join(recipe_book[dish])}\n"

    return result.strip()


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))




