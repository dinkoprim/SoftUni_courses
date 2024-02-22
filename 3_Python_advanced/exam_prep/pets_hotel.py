def accommodate_new_pets(capacity, max_weight, *pet_info):
    kennel = {}
    result = []
    available_capacity = capacity

    for pet_type, weight in pet_info:
        if not available_capacity:
            result.append("You did not manage to accommodate all pets!")
            break
        if weight <= max_weight:
            if pet_type not in kennel:
                kennel[pet_type] = [weight]
            else:
                kennel[pet_type].append(weight)

            available_capacity -= 1

    else:
        result.append(f"All pets are accommodated! Available capacity: {available_capacity}.")

    kennel = dict(sorted(kennel.items()))
    accommodated_pets = [f"{k}: {len(v)}" for k, v in kennel.items()]

    result.append("Accommodated pets:")
    for el in accommodated_pets:
        result.append(el)

    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
