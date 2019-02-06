# Song-Lyric-Scraper

# How it works
The user enters an artist and a song which they want the lyrics of, A get request is then made to the Genius api which checks if the url containing the song lyrics exist. If the url exists the scraper function scrapes the url and prints the lyrics to the users terminal. The user is also asked if they'd like information about the albums that the song is on, if the user says yes then a get request is also made to the Spotify api and prints the list of albums along with the year of release, album type(single,compilation or album) and the record label.

