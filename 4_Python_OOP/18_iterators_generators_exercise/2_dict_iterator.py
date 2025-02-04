class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = list(dictionary.items())
        self.idx = -1
        self.length = len(self.dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.dictionary) - 1:
            raise StopIteration()

        self.idx += 1
        return self.dictionary[self.idx]


# result = dictionary_iter({"name": "Peter", "age": 24})
# for x in result:
#     print(x)
