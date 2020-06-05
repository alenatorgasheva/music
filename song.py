class Song:
    """Класс песен"""

    def __init__(self, singer, name, duration):
        """Инициализация"""
        self.__name = name
        self.__singer = singer
        self.duration = Song.seconds(duration)

    def __str__(self):
        """Строковое представление"""
        return '{} - {}'.format(self.__singer, self.__name)

    @staticmethod
    def seconds(t):
        """Перевод минут в секунды"""
        min, sec = map(int, t.split(':'))
        sec += min * 60
        return sec
