# Project - study
# Audio player

# Developed by A.Torgasheva

# Существует множество веб-сайтов, на которых вы можете послушать музыку.
# Как правило, там представлены альбомы, содержащие треки. Каждый трек
# имеет название, продолжительность, имя исполнителя, год выпуска альбома
# и другие данные. Разработайте классы для альбомов и треков. Подумайте и
# реализуйте методы, которые могут воспроизводить трек, "ставить трек на
# паузу", останавливать воспроизведение треков и выполнять другие действия.

import time


class Load:
    """ """

    @classmethod
    def load_album(cls, fl_album):
        """ """
        with open(fl_album, 'r') as file_in:
            data = file_in.readlines()
        new_album = Album()
        for song in data:
            singer, name, duration = song.split(' - ')
            new_album.add_song(Song(singer, name, duration))


class Song:
    """ """

    def __init__(self, singer, name, duration):
        """ """
        self.__name = name
        self.__singer = singer
        self.__duration = Song.seconds(duration)

    @staticmethod
    def seconds(t):
        min, sec = map(int, t.split(':'))
        sec += min * 60
        return sec


class Album:
    """ """
    all_albums = []
    name = property()
    album = property()

    def __init__(self, name='Unknown'):
        """ """
        self.__album = []
        self.__name = name
        Album.all_albums.append(self)

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @album.getter
    def album(self):
        return self.__album

    def add_song(self, song):
        """ """
        self.__album.append(song)

    def del_song(self, song_name):
        for song in self.__album:
            if song.name == song_name:
                self.__album.remove(song)
                print('Песня удалена.')
                return
        print('Песня не найдена.')
        return


class Player:
    """ """
    def __init__(self):
        """ """
        self.playlist = []
        self.play_start = 0
        self.pause_start = 0
        self._play = False
        self._pause = False

    def add_song(self, song):
        """ """
        self.playlist.append(song)

    def add_album(self, album):
        """ """
        for song in album:
            self.playlist.append(song)

    def clear(self):
        self.playlist = []
        self.play_start = 0
        self.pause_start = 0
        self._play = False
        self._pause = False

    def play(self, album):
        """ """
        print('PLAY')
        t = time.time()
        if self._pause:
            self._pause = False
            self.play_start += (t - self.pause_start)
        self.play_start = t
        self._play = True

    def now_playing(self):
        """ """
        if self.play:
            t = time.time()
            duration = 0
            for i in range(len(self.playlist)):
                song = self.playlist[i]
                duration += song.__duration
                if t - (self.play_start + self.pause) < duration:
                    return song
        self._play = False
        self._pause = False
        return None

    def pause(self):
        """ """
        print('PAUSE')
        self.pause_start = time.time()
        self._pause = True

    def stop(self):
        """ """
        print('STOP')
        self.play_start = 0
        self.pause_start = 0
        self._play = False
        self._pause = False

