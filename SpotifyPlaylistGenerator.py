# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# import cred
#
# scope = "user-read-recently-played"
# scope = "playlist-modify-public"
#
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret=cred.client_SECRET,
#                                                redirect_uri=cred.redirect_url, scope=scope))
#
# results = sp.current_user_recently_played()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])
#
# playlist_name = 'Test'
#
# sp.user_playlist_create(cred.user_name, name=playlist_name)

import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import cred

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=cred.redirect_URI,
        client_id=cred.client_ID,
        client_secret=cred.client_SECRET,
        cache_path="token.txt"
    )
)

input_song = input("What song would you like to create a playlist based off of? Enter your response in the 'song name-artist name' format: ")
song_name = input_song.split("-")[0]
artist_name = input_song.split("-")[1]

artist_name = artist_name.title()

print(song_name)
print(artist_name)

# aerials-system of a down

musicstax_url = f"https://musicstax.com/search?q={song_name}+{artist_name}"



response = requests.get(musicstax_url)
song_scrape = response.text

soup = BeautifulSoup(song_scrape, "html.parser")

div_tag = soup.find_all('div', class_='song-artist')
a_tag = div_tag.find_parent('a')
a_tag = soup.find('a', id='some_id')
link = a_tag.get('href')

# div_tag = soup.find("div", string="System Of A Down")
# parent_tag = div_tag.parent
# href = parent_tag.get("href")
# print(href)

# a_string = soup.find(string="System Of A Down")
# a_string.find_parents("a")
# print(a_string)

# tag = soup.find_all("div", string="song")
# print(tag)

# # Find the tag containing the name of the artist (in this case, a span tag with class "artist-name")
# artist_tag = soup.find("div", class_=artist_name)
# print(artist_tag)

# # Access the parent tag of that tag (in this case, an a tag with class "track-link")
# parent_tag = artist_tag.parent
#
# # Extract the href attribute from that tag (in this case, "/track/6PQ88X9TkUIAUIZJHW2upE")
# href = parent_tag.get("href")
#
# # Print href value
# print(href)

# tag = soup.select(["a", "div", ])
# # tag = soup.find(id="link3")
# print(tag)

# print(soup.find(str.title(artist_name)))
# song_link = soup.find_all()
# if soup.select("[class~=song-details search-song-details]"):
#     return
# searches for a class with the name song-details search-song-details
# now i want to search for text within that class
# if a class has this text, return the parent class
# then take the link from the parent class and extract the last part of the string

# for link in soup.find_all('a'):
#     print(link.get('href'))





# SONG_YEAR = input("What year would you like to travel back to? Enter YYYY-MM-DD format: ")
# BILL_BOARD_URL = f"https://www.billboard.com/charts/hot-100/{SONG_YEAR}/"
# SONG_YEAR_YEAR = SONG_YEAR.split("-")[0]
# response = requests.get(BILL_BOARD_URL)
# song_scrape = response.text
#
# soup = BeautifulSoup(song_scrape, "html.parser")
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
# # pprint(song_artist_list)
#
#
# results = sp.current_user()
# # pprint(results)
# user_id = results['id']
#
# # print(results)
# # print(user_id)
#
# spotify_song_uris = []
# ##TAKEN OUT OF BELOW FOR LOOP ['artists'][0] -> remember to add back in
# for key, value in song_artist_list.items():
#     spotify_result = sp.search(q=f"artist:{key} track:{value} year:{SONG_YEAR_YEAR}", type="track")
#     try:
#         song_uri = spotify_result['tracks']['items'][0]['uri']
#         spotify_song_uris.append(song_uri)
#     except IndexError:
#         print(f"{value} doesn't exist in Spotify. Skipped.")
#
# print(len(spotify_song_uris))
#
# my_playlist = sp.user_playlist_create(user=f"{user_id}", name=f"{SONG_YEAR} Billboard Top Tracks", public=False,
#                                       description="Top Tracks from back in the Dayz of Brunel")
