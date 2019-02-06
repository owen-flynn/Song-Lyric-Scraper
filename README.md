# Song-Lyric-Scraper

# How It Works
The user enters an artist and a song which they want the lyrics of, A get request is then made to the Genius API which checks if the url containing the song lyrics exist. If the url exists the scraper function scrapes the url and prints the lyrics to the users terminal. The user is also asked if they'd like information about the albums that the song is on, if the user says yes then a get request is also made to the Spotify API and prints the list of albums along with the year of release, album type(single,compilation or album) and the record label.

# Running The Project
This Project was intended to be a practice project for me to get some experience with public api's and web scraping. If you'd like to run it however, then you can download the repo and run Python3 run.py. In order for it to work you'll need to make an account with Genius and Spotify, and follow the instructions for getting access tokens in order to authenticate your requests with each API. I also used the Beautiful Soup Library for web scraping and the Spotipy library for making Spotipy requests, It is reccomended to store access tokens in environemnt variables for security reasons and the Spotipy docs has instructions for doing this, you can set your Genius client secret in the same way. 

# links
[Genius API](https://docs.genius.com/)\
[Spotify API](https://developer.spotify.com/documentation/web-api/)\
[Spotipy Docs](https://spotipy.readthedocs.io/en/latest/)\
[Beautiful Soup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)


