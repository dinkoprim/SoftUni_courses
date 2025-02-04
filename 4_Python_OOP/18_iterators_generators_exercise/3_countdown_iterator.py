class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration()
        self.index =