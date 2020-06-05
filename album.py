class Album:
    """Класс альбомов"""
    lst_albums = []
    name = property()
    album = property()
    count_unknown = 0

    def __init__(self, name):
        """Инициализация"""
        self.__album = []
        if name:
            self.__name = name
        else:
            Album.count_unknown += 1
            self.__name = 'Unknown({})'.format(Album.count_unknown)
        Album.lst_albums.append(self)

    def __str__(self):
        """Строковое представление"""
        s = self.__name + '\n'
        for song in self.__album:
            s += '{}\n'.format(song)
        return s

    def __repr__(self):
        """Представление"""
        return self.name

    @album.getter
    def album(self):
        """Получение списка песен аольбома"""
        return self.__album

    @name.setter
    def name(self, new_name):
        """Изменение названия аольбома"""
        self.__name = new_name

    @name.getter
    def name(self):
        """Получение названия аольбома"""
        return self.__name

    def add_song(self, song):
        """Добавление песен в альбом"""
        self.__album.append(song)

    def del_song(self, song_name):
        """Удаление песни из альбома"""
        for song in self.__album:
            if song.name == song_name:
                self.__album.remove(song)
                print('Песня удалена.')
                return
        print('Песня не найдена.')
        return

    @classmethod
    def find_album(cls, name):
        """Нахождение альбома"""
        for alb in cls.lst_albums:
            if alb.name.lower() == name.lower():
                return alb
        return None
