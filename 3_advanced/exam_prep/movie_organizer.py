def movie_organizer(*name_genre_pairs):
    collection = {}

    for name, genre in name_genre_pairs:
        if genre not in collection.keys():
            collection[genre] = []
        collection[genre].append(name)

    collection = dict(sorted(collection.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''
    for genre, names in collection.items():
        sorted_movies = sorted(names)
        result += f"{genre} - {len(sorted_movies)}\n"
        for name in sorted_movies:
            result += f"* {name}\n"
    return result.strip()

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))


