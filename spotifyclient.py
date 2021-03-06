import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def create_spotipy_object():
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return sp

def get_song_data(song_title,sp):
    url = "https://api.spotify.com/v1/search"
    response = sp.search(song_title, limit=50, offset=0, type='track', market=None)

    return response

def get_album_ids(song_data,artist_name,song_title):
    ids = {}
    data = song_data["tracks"]["items"]

    for song in data:
        if song["artists"][0]["name"] == artist_name:
            ids[song["album"]["name"]] = song["album"]["id"]

    return ids

def get_album_data(album_id,sp):
    url = "https://api.spotify.com/v1/albums/" + album_id
    response = sp.album(album_id)

    return response

def appears_on(song_title,album_ids,sp):
    print(song_title," appears on the following albums:")

    for album , album_id in album_ids.items():
        data = get_album_data(album_id,sp)
        album_type = data["album_type"]
        release_date = data["release_date"][:4]
        label = data["label"]

        print(album,album_type,release_date,label)
