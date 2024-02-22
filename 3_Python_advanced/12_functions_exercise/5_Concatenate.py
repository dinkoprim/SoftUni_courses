def concatenate(*args, **kwargs):
    words = ''.join(args)
    for key, value in kwargs.items():
        words = words.replace(key, value)
    #     start = 0
    #     while key in words[start:]:
    #         start = words.index(key, start)
    #         end = start + len(key)
    #         words = words[:start] + value + words[end:]
    #         start += len(value)
    return words


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
