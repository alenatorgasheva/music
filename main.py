# Project - study
# Audio player

# Developed by A.Torgasheva

from load import Load
from player import Player
from song import Song
from album import Album

MENU = 'Выбрите действие:\n' \
       '\t1 - загрузить альбом\n' \
       '\t2 - изменить название альбома\n' \
       '\t3 - действия с плейлистом\n' \
       '\t4 - действия с плеером\n' \
       '\t5 - завершить работу'

PLAYLIST = '\t1 - просмотреть плейлист\n' \
           '\t2 - добавить песню\n' \
           '\t3 - добавить альбом\n' \
           '\t4 - удалить песню\n' \
           '\t5 - очистить плейлист'

PLAYER = '\tPLAY (1)\n' \
         '\tPAUSE (2)\n' \
         '\tSTOP (3)\n' \
         '\tсейчас играет (4)\n' \
         '\tвыйти в главное меню (5)'

playlist_1 = Player()
while True:
    print(MENU)
    choice = input()
    print('-' * 100)

    if choice == '1':
        print('Название файла:', end=' ')
        file_name = input()
        print('Название альбома:', end=' ')
        name = input()
        Load.load_album(file_name, name)
        print('Альбом загружен.')

    elif choice == '2':
        print('Старое название:', end=' ')
        old_name = input()
        album = Album.find_album(old_name)
        if album:
            print('Новое название:', end=' ')
            new_name = input()
            album.name = new_name
            print('Название альбома изменено.')
        else:
            print('Альбом не найден')

    elif choice == '3':
        print(PLAYLIST)
        choice = input()
        print('-' * 100)

        if choice == '1':
            print(playlist_1)

        elif choice == '2':
            print('Ипсолнитель:', end=' ')
            singer = input()
            print('Название песни:', end=' ')
            name = input()
            song = Song.find_song(singer, name)
            if song:
                playlist_1.add_song(song)
                print('Песня добавлена.')
            else:
                print('Песня не найдена.')

        elif choice == '3':
            print('Доступные альбомы:', Album.lst_albums)
            print('Название альбома:', end=' ')
            name = input()
            album = Album.find_album(name)
            if album:
                playlist_1.add_album(album)
                print('Альбом добавлен.')
            else:
                print('Альбом не найден')

        elif choice == '4':
            print('Ипсолнитель:', end=' ')
            singer = input()
            print('Название песни:', end=' ')
            name = input()
            song = Song.find_song(singer, name)
            if song:
                playlist_1.del_song(song)
                print('Песня удалена.')
            else:
                print('Песня не найдена.')

        elif choice == '5':
            playlist_1.clear()
            print(playlist_1)

    elif choice == '4':
        while True:
            print(PLAYER)
            choice = input()
            if choice == '1':
                playlist_1.play()
            elif choice == '2':
                playlist_1.pause()
            elif choice == '3':
                playlist_1.stop()
            elif choice == '4':
                print(playlist_1.now_playing())
            elif choice == '5':
                break
            print('-' * 100)

    elif choice == '5':
        break

    print('-' * 100)

print('Работа завершена.')
