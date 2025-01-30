from mystuff import MyStuff
from song import Song

# Using the MyStuff class
thing = MyStuff()
thing.apple()
print(thing.tangerine)

# Using the Song class
happy_bday_lyrics = ["Happy birthday to you",
                     "I don't want to get sued",
                     "So I'll stop right there"]
bulls_on_parade_lyrics = ["They rally around tha family",
                          "With pockets full of shells"]

happy_bday = Song(happy_bday_lyrics)
bulls_on_parade = Song(bulls_on_parade_lyrics)

# Singing the songs
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()


