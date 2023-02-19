import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from pprint import pprint

SPOTIFY_CLIENT_ID = "069b12c4bbea439baeac8a3a3a519be1"
SPOTIFY_SECRET = "624a20be2ac149b88539f012771d8ce7"
REDIRECT_URL = "https://localhost:8888/callback"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URL,
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_SECRET,
        cache_path="token.txt"
    )
)

# SONG_YEAR = input("What year would you like to travel back to? Enter YYYY-MM-DD format: ")
# BILL_BOARD_URL = f"https://www.billboard.com/charts/hot-100/{SONG_YEAR}/"
# SONG_YEAR_YEAR = SONG_YEAR.split("-")[0]
# print(SONG_YEAR_YEAR)
#
# response = requests.get(BILL_BOARD_URL)
# song_scrape = response.text
#
# soup = BeautifulSoup(song_scrape, "html.parser")
#
# song_tags_list = soup.findAll(name="h3", class_="a-no-trucate")
# artists_tags_list = soup.findAll(name="span", class_="a-no-trucate")
#
#
# song_list_1 = [tag.getText().replace("\n", "") for tag in song_tags_list]
# song_list_2 = [song.replace("\t", "") for song in song_list_1]
#
# artist_list_1 = [tag.getText().replace("\n", "") for tag in artists_tags_list]
# artist_list_2 = [artist.replace("\t", "") for artist in artist_list_1]
#
# song_artist_list = dict(zip(artist_list_2, song_list_2))
# pprint(song_artist_list)
#
#
# results = sp.current_user()
# pprint(results)
# user_id = results['id']
#
# print(results)
# print(user_id)

spotify_song_uris = []
# TAKEN OUT OF BELOW FOR LOOP ['artists'][0] -> remember to add back in
for key, value in song_artist_list.items():
    spotify_result = sp.search(q=f"artist:{key} track:{value} year:{SONG_YEAR_YEAR}", type="track")
    try:
        song_uri = spotify_result['tracks']['items'][0]['uri']
        spotify_song_uris.append(song_uri)
    except IndexError:
        print(f"{value} doesn't exist in Spotify. Skipped.")

print(len(spotify_song_uris))

# my_playlist = sp.user_playlist_create(user=f"{user_id}", name=f"test", public=False, description="test")