import random
from urllib.request import urlopen
import sys

WORLD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
	  "Make a class named %%% that is-a %%%",
	"class %%%(object):\n\tdef__init__(self, ***)":
	  "class %%% has-a __init__ that takes self and @@@ parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)":
	  "class %%% has-a function named *** that takes self and @@@ parameters.",
	"*** = %%%()":
	  "Set *** to an intance of class %%%.",
	"***.***(@@@)":
	  "From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	  "From *** get the *** attribute and set it to '***'"
}

PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True

for word in urlopen(WORLD_URL).readlines():
	WORDS.append(word.strip().decode("utf-8")) # Put the url's words inot WORDS[]

def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
				   random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		for word in class_names:
			result = result.replace("%%%", word, 1)

		for word in other_names:
			result = result.replace("***", word, 1)

		for word in other_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results

try:
	while True:
		snippets = list(PHRASES.keys()) # In python 3 : keys() will return an object, but shuffle() need to input a list
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print("question")

			input("> ")
			print("ANSWER: {}\n\n".format(answer))
except EOFError:
	print("\nBye")