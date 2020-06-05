import time


class Player:
    """Класс проигрывателя"""

    def __init__(self):
        """Инициализация"""
        self.playlist = []
        self.play_start = 0
        self.duration = 0
        self._play = False
        self._pause = False

    def __str__(self):
        """Строковое представление"""
        if self.playlist:
            s = 'Плейлист:\n'
            for song in self.playlist:
                s += '{}\n'.format(song)
        else:
            s = 'Плейлист пуст.'
        return s

    def add_song(self, song):
        """Добавление песен в плеер"""
        self.playlist.append(song)

    def add_album(self, alb):
        """Добавление альбома в плеер"""
        for song in alb.album:
            self.playlist.append(song)

    def del_song(self, song):
        """Удаление песни из плеера"""
        self.playlist.remove(song)

    def clear(self):
        """Удаление всех песен из плеера"""
        self.playlist = []
        self.play_start = 0
        self.duration = 0
        self._play = False
        self._pause = False

    def now_playing(self):
        """Получение песни, играющей на данный момент"""
        t = self.duration + (time.time() - self.play_start)
        for song in self.playlist:
            t -= song.duration
            if t <= 0:
                return 'Сейчас играет:\n\t{}'.format(song)
        return 'Сейчас ничего не играет.'

    def play(self):
        """Метод 'PLAY'"""
        print('PLAY')
        self.play_start = time.time()
        self._play = True
        self._pause = False

    def pause(self):
        """Метод 'PAUSE'"""
        print('PAUSE')
        self.duration = time.time() - self.play_start
        self._play = False
        self._pause = True

    def stop(self):
        """Метод 'STOP'"""
        print('STOP')
        self._play = False
        self._pause = False
        self.play_start = 0
