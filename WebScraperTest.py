import requests
from bs4 import BeautifulSoup
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
for link in soup.find_all('a'):
    print(link.get('href'))