

am an intermediate level Python programmer. This is my implementation of a MP3 Playlist class challenge that was hosted on 101 Computing.Net. The goal of the challenge was to implement a Class in Python to maintain an MP3 Playlist. The key features of the class are the ability to:

Enqueue an MP3 to the playlist
Remove an MP3 from the playlist
Load a playlist from a text file
Save a playlist on a text file
Shuffle all the songs in the playlist
Display all the tracks from the playlist
Count the number of tracks in the playlist
Calculate the total duration of the playlist
Empty/Reset the playlist
Check if the playlist is empty

import os
import sys
import datetime
from random import shuffle
from track import Track


class MP3PlayList:
    """A MP3Playlist class."""

    def __init__(self, title: str, filename: str) -> None:
        """Initialize attributes."""
        self.title = title
        self.filename = filename
        self.tracks = []

    def __repr__(self) -> str:
        """String representation the class."""
        return f'{self.__class__.__name__}(title={self.title}, filename={self.filename}, tracks={self.tracks})'

    def load_playlist(self):
        """Loads a saved playlist, and displays its contents"""
        if not os.path.isfile(os.path.join('music_files', self.filename)):
            print(f'{self.title} could not be loaded.\n{self.filename} does not exists!', file=sys.stderr)
        else:
            with open(os.path.join('music_files', self.filename)) as file_obj:
                song_list = [i.strip().split(',') for i in file_obj]
            for song in song_list:
                self.add_track(Track(song[0], song[1], song[2]))
            self.show_playlist()

    def save_playlist(self, filename=None):
        """Saves the current playlist in a textfile"""
        self.filename = self.filename if filename is None else filename

        with open(os.path.join('music_files', self.filename), 'w+') as file_object:
            for track in self.tracks:
                song, artist, duration = track.title, track.artist, track.duration
                file_object.write(f'{song},{artist},{duration}' + '\n')
        print(f'{self.title} has been successfully saved.')

    def add_track(self, track):
        """Add a single track to the playlist."""
        self.tracks.insert(0, track)
        print(f'"{track.title}" has been added successfully!')

    def remove_track(self, track_name):
        """Removes a track from the playlist"""
        is_located = False
        for i, track in enumerate(self.tracks):
            if track_name == track.title:
                self.tracks.pop(i)
                print(f'"{track_name}" has been successfully removed.')
                is_located = True
        if not is_located:
            print(f'"{track_name}" could not be located. Please try again.')

    def show_playlist(self):
        """Displays entire playlist, including title, artist, and duration."""
        if self.tracks:
            print('Track list:')
            for track in self.tracks:
                song, artist, duration = track.title, track.artist, track.duration
                print(f'\t• {song} - {artist} ({duration})')
        else:
            print('Track list is empty!')

    def shuffle_playlist(self, n):
        """Shuffles playlist n x"""
        if self.tracks:
            for i in range(n):
                shuffle(self.tracks)
            print(f'Playlist was shuffled {n}xs!')
        else:
            print('Playlist could not be found.')

    def get_number_of_tracks(self):
        """Prints the total number of tracks stored in the playlist."""
        print(f'Total tracks: {len(self.tracks)}')

    def get_total_duration(self):
        """Prints the total duration time of all tracks."""
        current_year = datetime.datetime.now().year
        datetime_original = datetime.datetime(year=current_year, month=1, day=1)
        for track in self.tracks:
            minutes, seconds = [int(i) for i in track.duration.split(':')]
            datetime_original += datetime.timedelta(minutes=minutes, seconds=seconds)
        print('Total duration: {:%H:%M:%S}'.format(datetime_original))

    def reset_playlist(self):
        """Clears the playlist."""
        self.tracks.clear()
        print(f'{self.title} has been reset.')

    def is_empty(self):
        """Returns True if playlist is empty, False otherwise"""
        return len(self.tracks) == 0
    


class Track:
    """A Track class"""

    def __init__(self, title, artist, duration):
        """Initialize attributes."""
        self.title = title
        self.artist = artist
        self.duration = duration

    def __repr__(self):
        return f'{self.__class__.__name__}(title={self.title}, artist={self.artist}, duration={self.duration} seconds)'

from mp3playlist import MP3PlayList, Track


def main():
    # Initialize Playlist:
    mp3_playlist = MP3PlayList('MyCoolMusic', 'music_playlist.txt')

    # Check if empty:
    print(mp3_playlist.is_empty())  # True

    # Load playlist from textfile:
    mp3_playlist.load_playlist()

    # Remove a track by title
    mp3_playlist.remove_track('one')

    # Add a new track:
    track = Track('metallica', 'the unforgiven', '6:23')
    mp3_playlist.add_track(track)

    # Informs user if file cannot be found:
    mp3_playlist.remove_track('bogus_file')  # File cannot be located!

    # Shuffles list 3 x times:
    mp3_playlist.shuffle_playlist(3)

    # Get total number of tracks:
    mp3_playlist.get_number_of_tracks()

    # Get total duration of playlist
    mp3_playlist.get_total_duration()

    # Save Playlist and filename by name designated at instance initialization
    mp3_playlist.save_playlist()

    # Shuffle list 7x times:
    mp3_playlist.shuffle_playlist(7)

    # Create a file with a new custom file_name:
    mp3_playlist.save_playlist('backup_copy.txt')


if __name__ == '__main__':
    main()