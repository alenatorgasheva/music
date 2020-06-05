class Album:
    """Класс альбомов"""
    all_albums = []
    name = property()
    album = property()

    def __init__(self, name='Unknown'):
        """Инициализация"""
        self.__album = []
        self.__name = name
        Album.all_albums.append(self)

    def __str__(self):
        """Строковое представление"""
        s = self.__name + '\n'
        for song in self.__album:
            s += '{}\n'.format(song)
        return s

    @name.setter
    def name(self, new_name):
        """Изменение имени"""
        self.__name = new_name

    @album.getter
    def album(self):
        """Получение списка песен из альбома"""
        return self.__album

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
