#https://spotipy.readthedocs.io/en/2.22.1/
#https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth
#https://spotipy.readthedocs.io/en/2.22.1/

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URL,
    show_dialog=True,
    cache_path="../../Day045/token.txt"
    ))

user_id = sp.current_user()["id"]

#==========================================================#
URL_INITIAL = "https://www.billboard.com/charts/hot-100/"
URL_DATE = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = URL_INITIAL + URL_DATE

response = requests.get(URL)
bb_web_page = response.text

soup = BeautifulSoup(bb_web_page, "html.parser")
songs = soup.select("li ul li h3#title-of-a-story")

song_titles = [song.getText(strip=True) for song in songs]

#==========================================================#

song_uris = []
year = URL_DATE.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#==========================================================#
playlist = sp.user_playlist_create(user=SPOTIFY_USER_ID, name=f"{URL_DATE} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
