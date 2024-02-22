entry_count = int(input())
entries_list = [input() for i in range(entry_count)]


def barcode_validator(sequence):
    for element in sequence:
        is_valid = True
        if '#' in element:
            no_hashtags = element.replace('#', '')
            if not no_hashtags.startswith("@") and not no_hashtags.endswith("@"):
                is_valid = False
            else:
                content = no_hashtags[1:-1]
                if len(content) < 6:
                    is_valid = False
                elif not content[0].isupper():
                    is_valid = False
                elif not content.isalnum():
                    is_valid = False
                elif not content[-1].isupper():
                    is_valid = False
        else:
            is_valid = False

        if is_valid:
            digits_only = ''.join([char for char in element if char.isdigit()])
            if digits_only:
                product_group = digits_only
            else:
                product_group = '00'
            print(f"Product group: {product_group}")
        else:
            print("Invalid barcode")


result = barcode_validator(entries_list)



