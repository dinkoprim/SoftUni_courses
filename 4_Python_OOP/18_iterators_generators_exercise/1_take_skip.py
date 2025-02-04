class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.turn = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.turn == self.count - 1:
            raise StopIteration()

        self.turn += 1
        return self.turn * self.step

# numbers = take_skip(2, 6)
# for number in numbers:
#     print(number)
