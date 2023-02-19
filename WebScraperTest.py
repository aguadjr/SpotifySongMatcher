import requests
from bs4 import BeautifulSoup

# user inputs song and the input is split up
input_song = input("What song would you like to create a playlist based off of? Enter your response in the 'song name-artist name' format: ")
song_name = input_song.split("-")[0]
artist_name = input_song.split("-")[1]

# test songs:
# aerials-system of a down
# master of puppets-metallica
# lateralus-tool

# find the musicstax page for input song and parse it
musicstax_url = f"https://musicstax.com/search?q={input_song}"
response = requests.get(musicstax_url)
song_scrape = response.text
soup = BeautifulSoup(song_scrape, "html.parser")

# find the 'a' tag with the class 'song-details-right'
a_tag = soup.find('a', class_='song-details-right')

# get the link within the 'a' tag we found and print it
link = a_tag.get('href')
print(link)

# split the link we found up so that we get the song name and string at the end and print it
track = link.split("track")[1]
print(track)

# find the musicstax page for similar songs to the track we input
musicstax_url2 = f"https://musicstax.com/track/similar{track}"
response2 = requests.get(musicstax_url2)
song_scrape2 = response2.text
soup2 = BeautifulSoup(song_scrape2, "html.parser")

# find all links under the 'a' tag with the class artist-seed-track-right
for link in soup2.find_all('a', class_='artist-seed-track-right'):
    similar_track = link.get('href')
    similar_track_name = similar_track.split("/")[2]
    print(similar_track_name)