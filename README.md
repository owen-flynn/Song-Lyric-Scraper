# Song-Lyric-Scraper

# How It Works
This is a simple command line based project which allows the user to enter the name of an Artist and a Song and get the lyrics for that song. The user is also prompted to specify if they would like information on the albums on which the song appears. When the user enters the Artist and Song, a get request is made to the Genius API for the URL of the songs lyrics. if the URL exists, the scraper function then scrpaes the URl for the lyrics and the lyrics are printed to the terminal. If the User requests album information as well then a get request is sent to the Spotify API and a list of Albums that the song appears on as well as the album type(single,album or compilation), relaese year and the record label is printed to the users terminal also.

#Libraries Used
I made use of the BeautifulSoup library [Beautiful Soup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to aid with the web scraping, as well as the Spotipy Library [Spotipy Docs](https://spotipy.readthedocs.io/en/latest/) which is a Python library for making Spotify API requests


# links
[Genius API](https://docs.genius.com/)\
[Spotify API](https://developer.spotify.com/documentation/web-api/)\
