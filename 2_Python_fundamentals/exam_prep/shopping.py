stores = {}
all_items = []


def add_item(store, items):
    global all_items
    if store not in stores:
        stores[store] = {'items': [], 'important_item': False}
    for item in items:
        if item not in all_items:
            all_items.append(item)
            if item not in stores[store]['items']:
                stores[store]['items'].append(item)


def add_important_item(store, item):
    global all_items
    if store not in stores:
        stores[store] = {'items': [], 'important_item': True}
    if item not in all_items:
        all_items.append(item)
        if item not in stores[store]['items']:
            stores[store]['items'].insert(0, item)
            stores[store]['important_item'] = True


def remove_store(store):
    global all_items
    if store in stores and not stores[store]['important_item']:
        for item in stores[store]['items']:
            all_items.remove(item)
        del stores[store]


def print_stores():
    for store, data in stores.items():
        print(f"{store}:")
        for item in data['items']:
            print(f"  - {item}")


while True:
    command = input().split("->")
    if command[0] == "Go Shopping":
        break
    action, store = command[0], command[1]
    if action == "Add":
        items = command[2].split(",")
        add_item(store, items)
    elif action == "Important":
        item = command[2]
        add_important_item(store, item)
    elif action == "Remove":
        remove_store(store)

print_stores()
