from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)

        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        try:
            album_to_remove = next(filter(lambda a: a.name == album_name, self.albums))
        except StopIteration:
            return f"Album {album_name} is not found."

        if album_to_remove.published:
            return f"Album has been published. It cannot be removed."

        self.albums.remove(album_to_remove)
        return f"Album {album_name} has been removed."

    def details(self):
        output = f'Band {self.name}'
        for album in self.albums:
            output += f'\n{album.details()}'
        return output

