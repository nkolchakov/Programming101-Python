import time
from random import randint


class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist = []
        self.size = len(self.playlist)
        self.current_song_index = 0
        self._played_songs = []

    def add_song(self, song):
        if song not in self.playlist:
            self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.playlist.append(song)

    def total_length(self):
        total = 0
        for song in self.playlist:
            total += song.get_length(seconds=True)
        return 'Total playlist time: {}'.format(time.strftime('%H:%M:%S',
                                                time.gmtime(total)))

    def artists(self):
        histogram = {}
        for song in self.get_playlist():
            if song.artist in histogram:
                histogram[song.artist] += 1
            else:
                histogram[song.artist] = 1

    def next_song(self):
        if self.shuffle:
            self.next_suffle_song()
        else:
            next_song = self.playlist[self.current_song_index]
            self.current_song_index += 1
            if self.current_song_index == self.size: # gurmi
                if self.repeat:
                    self.current_song_index = 0
                else:
                    return 'end.'
            return next_song

    def next_suffle_song(self):
        if self.size == 0:
            if self.repeat:
                self._played_songs = []
            else:
                return 'all songs were played'
            self._played_songs = []
        random_index = randint(0, len(self.size - 1))
        while True:
            if self.playlist[random_index] not in self.played_songs:
                self._played_songs.append(self.playlist[random_index])
                return self.playlist[random_index]
            else:
                random_index = (random_index + 1) % self.size

    def get_playlist(self):
        return self.playlist

    def pprint_playlist(self):
        # print table like
        pass

    def save(self):
        pass

    @staticmethod
    def load(self):
        pass

