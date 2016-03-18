from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from song import Song
from os import listdir
from os.path import isfile, join


class MusicCrawler:
    def __init__(self, music_path):
        # /home/kolchakov/Desktop/mp3/CD1/
        self.__music_path = music_path
        self.__generated_playlist = []

    def generate_playlist(self):
        song_names = [f for f in listdir(self.__music_path) if isfile(join(self.__music_path, f))]
        for song in song_names:
            audio = MP3("/home/kolchakov/Desktop/mp3/CD1/{}".format(
                        song), ID3=EasyID3)
            s_name = audio['title'][0]
            s_artis = audio['artist'][0]
            s_album = audio['album'][0]
            seconds = '{:.0f}'.format(audio.info.length)
            generated_song = Song(s_name, s_artis, s_album, seconds)
            self.__generated_playlist.append(generated_song)
        return self.__generated_playlist

