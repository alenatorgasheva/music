class Song:
    """Класс песен"""
    lst_songs = []

    def __init__(self, singer, name, duration):
        """Инициализация"""
        self.__name = name
        self.__singer = singer
        self.duration = Song.seconds(duration)
        Song.lst_songs.append(self)

    def __str__(self):
        """Строковое представление"""
        return '{} - {}'.format(self.__singer, self.__name)

    @staticmethod
    def seconds(t):
        """Перевод минут в секунды"""
        min, sec = map(int, t.split(':'))
        sec += min * 60
        return sec

    @classmethod
    def find_song(cls, singer, name):
        """Нахождение песни"""
        for song in cls.lst_songs:
            if song.__singer.lower() == singer.lower() and song.__name.lower() == name.lower():
                return song
        return None
