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

    for i in range(0,len(data)):
        if data[i]["artists"][0]["name"] == artist_name:
            ids[data[i]["album"]["name"]] = data[i]["album"]["id"]

    return ids

def appears_on(song_title,album_ids,sp):
    print(song_title," appears on the following albums:")

    for album in album_ids:
        album_id = album_ids[album]
        data = get_album_data(album_id,sp)
        release_date = data["release_date"][:4]
        print(album,data["album_type"],release_date,data["label"])

def get_album_data(album_id,sp):
    url = "https://api.spotify.com/v1/albums/" + album_id
    response = sp.album(album_id)

    return response
