sequence = [int(num) for num in input().split(', ')]
positives = [num for num in sequence if num >= 0]
negatives = [num for num in sequence if num < 0]
evens = [num for num in sequence if num % 2 == 0]
odds = [num for num in sequence if num % 2 != 0]
print(f"Positive: {str(positives)[1:-1]}"
      f"\nNegative: {str(negatives)[1:-1]}"
      f"\nEven: {str(evens)[1:-1]}"
      f"\nOdd: {str(odds)[1:-1]}")
