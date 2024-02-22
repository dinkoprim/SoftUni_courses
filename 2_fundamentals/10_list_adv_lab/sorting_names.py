def names_sorter(names):
    sorted_list = sorted(names, key=lambda x: (-len(x), x))
    return sorted_list


names_list = input().split(', ')
print(names_sorter(names_list))
