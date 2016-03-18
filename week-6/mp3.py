from music_crawler import MusicCrawler
from playlist import Playlist

def main():
    path = '/home/kolchakov/Desktop/mp3/CD1/'
    crawler = MusicCrawler(path)
    songs = crawler.generate_playlist()
    my_playlist = Playlist('rock')
    my_playlist.add_songs(songs)
    while True:
        command = input("enter command>>")
        if command == "next":
            print (my_playlist.next_song())


if __name__ == '__main__':
    main()