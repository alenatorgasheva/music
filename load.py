from album import Album
from song import Song


class Load:
    """Класс считывания данных"""

    @classmethod
    def load_album(cls, fl_album, name):
        """Загрузка альбома"""
        with open(fl_album, 'r') as file_in:
            data = file_in.readlines()
        new_album = Album(name)
        for song in data:
            singer, name, duration = song.split(' - ')
            new_album.add_song(Song(singer, name, duration))
