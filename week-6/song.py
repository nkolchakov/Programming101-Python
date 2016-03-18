from playlist import Playlist


class Song:
    def __init__(self, title, artist, album, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.length = length

    def __str__(self):
        return "{} - {} from {} - {}".format(
                self.artist, self.title, self.album, self.length)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.artist == other.artist and self.title == other.title

    def __hash__(self):
        return hash(str(self))

    def _transform_len(self, mode):
        # less parameters , out of range
        time = 0
        power = 0
        el = [int(x) for x in self.length.split(':')]
        for i in range(len(el)-1, -1, -1):
            time += el[i]*60**power
            power += 1
        return time

    def get_length(self, seconds=False, minutes=False, hours=False):
        mode = 'full'
        if seconds:
            mode = 's'
        elif minutes:
            mode = 'm'
        elif hours:
            mode = 'h'
        else:
            return self.length
        return self._transform_len(mode)



