from typing import List


def positive_sieve(nums: List[int]) -> None:
    positive_sum = sum(n for n in nums if n > 0)
    negative_sum = sum(n for n in nums if n < 0)

    print(negative_sum)
    print(positive_sum)

    if abs(positive_sum) > abs(negative_sum):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


line = [int(x) for x in input().split()]
positive_sieve(line)
