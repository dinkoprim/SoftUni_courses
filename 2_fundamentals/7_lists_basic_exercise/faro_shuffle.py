cards_deck = input().split()
shuffles_count = int(input())

for shuffle in range(shuffles_count):
    current_shuffle_deck = []
    middle_of_deck = len(cards_deck) // 2
    left_part = cards_deck[:middle_of_deck]
    right_part = cards_deck[middle_of_deck:]

    for card_index in range(len(left_part)):
        current_shuffle_deck.append(left_part[card_index])
        current_shuffle_deck.append(right_part[card_index])

    cards_deck = current_shuffle_deck
print(current_shuffle_deck)