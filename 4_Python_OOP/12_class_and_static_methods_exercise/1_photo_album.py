from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE = 4
    SYMBOLS_COUNT = 11
    SYMBOLS = '-'
    PAGE_SEPARATOR = SYMBOLS * SYMBOLS_COUNT

    def __init__(self, pages: int):
        self.pages = pages
        self.photos: List[List[str]] = []
        for _ in range(self.pages):
            self.photos.append([])

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / cls.PHOTOS_PER_PAGE))

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < self.PHOTOS_PER_PAGE:
                self.photos[page].append(label)
                slot = len(self.photos[page])
                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return f"No more free slots"

    def display(self):
        result = ''
        for page in range(len(self.photos)):
            result += f'{self.PAGE_SEPARATOR}\n'
            if self.photos[page]:
                result += ' '.join(['[]' for _ in range(len(self.photos[page]))]) + '\n'
            else:
                result += '\n'
        result += f'{self.PAGE_SEPARATOR}'
        return result


album = PhotoAlbum(5)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())



