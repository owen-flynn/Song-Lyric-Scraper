import geniusclient
import spotifyclient
import os

def print_album_info(artist_name,song_title):
    sp = spotifyclient.create_spotipy_object()
    song_data = spotifyclient.get_song_data(song_title,sp)
    album_ids = spotifyclient.get_album_ids(song_data,artist_name,song_title)
    spotifyclient.appears_on(song_title,album_ids,sp)

def main():
    client_access_token = os.environ.get('CLIENT_ACCESS_TOKEN')
    artist_name = input("please enter an artist to search for:\n")
    song_title = input("please enter a song to search for:\n")
    album_option = input("would you like album info for the song, yes or no ?:\n")
    song_data = geniusclient.get_song_data(song_title,client_access_token)
    url = geniusclient.get_url(artist_name,song_data)

    if url:
        if album_option == "yes":
            print_album_info(artist_name,song_title)
        lyrics = geniusclient.scrape(url)
        print(lyrics)
    else:
        print("No match")

if __name__ == "__main__":
    main()
