class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_ma_a_song(self):
		for line in self.lyrics:
			print(line)

happy_baby = Song(["Happy birthday to you",
	"I don't want to get sued",
	"So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
	"With pockets full of shells"])

happy_baby.sing_ma_a_song()

bulls_on_parade.sing_ma_a_song()