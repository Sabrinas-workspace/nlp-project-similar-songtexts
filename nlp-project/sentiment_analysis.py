import xml.etree.ElementTree as ET

import pandas as pd

import SongtextSentiment

import SongInformation

tree = ET.parse('D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_songtexts_genius.xml')

root = tree.getroot()

# for child in root:
#     text = child.find("songtext")
#     songtext = text.text
#     # print(SongtextSentiment.song_polarity(songtext))
#     print(SongtextSentiment.song_polarity_lines(songtext))
#     print(SongtextSentiment.pos_neg_neutral_polarity(songtext, root))
    
#     print("")

# print("")
# print(SongtextSentiment.similar_mood_polarity("Clouds", "NF", root))
# print("")
# print(SongtextSentiment.similar_mood_polarity("Paralyzed", "NF", root))
# print("")
# print(SongtextSentiment.similar_mood_polarity("Remember This", "NF", root))
# print("")
# print(SongtextSentiment.similar_mood_polarity("Returns", "NF", root))
# print("")
# print(SongtextSentiment.similar_mood_polarity("If you want love", "NF", root))
# print("")

# dataframe

songtitles = []
artists = []
songs_with_similar_mood = []


for child in root:
    songtitle = SongInformation.get_songtitle_child(child)
    artist = SongInformation.get_artist_child(child)
    similar_mood = SongtextSentiment.similar_mood_polarity_title(songtitle, artist, root)
    songtitles.append(songtitle)
    artists.append(artist)
    songs_with_similar_mood.append(similar_mood)


songs = {'Songtitle': songtitles,
         'Artist': artists,
         'Song with a similar mood': songs_with_similar_mood
        }

df = pd.DataFrame(songs, columns = ['Songtitle','Artist', 'Song with a similar mood'])

df.to_csv (r'D:/Data/Nextcloud/Documents/Uni/Advanced NLP with Python/AP Projekt/Data_sentiment.csv', sep= ';', index = False, header=True)

print (df)