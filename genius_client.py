import os
import requests
import json
from bs4 import BeautifulSoup

def get_song_data(song_title,client_access_token):
    base_url = "http://api.genius.com"
    headers = {'Authorization': 'Bearer ' + client_access_token}
    search_url = base_url + "/search"
    params = {'q': song_title}
    response = requests.get(search_url, params=params, headers=headers)
    json = response.json()

    return json

def get_url(artist_name,song_data):
    for hit in song_data["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist_name:
            return hit["result"]["url"]

    return None

def scrape(url):
    page_source = requests.get(url).text
    soup = BeautifulSoup(page_source, "html.parser")
    lyrics = soup.find("div",class_="lyrics").get_text()
    
    return lyrics
