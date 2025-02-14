import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
date = input("Which year do you want to travel to? Type the date in this Format YYYY-MM-DD: ")
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
URL = f"https://www.billboard.com/charts/hot-100/{date}/#"

CLIENT_ID = "9fc6e679910c4776bc50fa303c30cfd9"
CLIENT_SECRET = "fa9050dc8f5940919d16cff21ab780e4"
REDIRECT_URL = "http://example.com"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URL,
    scope="playlist-modify-private"
))

response = requests.get(URL, headers=headers)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.select("li ul li h3")
song_titles = [song.getText().strip() for song in all_songs]
print(" Top Songs:",song_titles)

def get_song_url(song_name):
    result = sp.search(q=song_name, limit=1)
    if result["tracks"]["items"]:
        return result["tracks"]["items"][0]["external_urls"]["spotify"]
    else:
        return None

song_urls = {song: get_song_url(song) for song in song_titles}

user_id = sp.current_user()["id"]

playlist = sp.user_playlist_create(user_id, "Billboard to Spotify", public=False, description='Takes 100 songs from the past and creates a new Spotify playlist based on the songs')
playlist_id = playlist["id"]
print(f"Playlist Created: {playlist['name']}")

sp.playlist_add_items(playlist_id=playlist_id, items=song_urls.values())

print("Songs Added to Playlist!")
