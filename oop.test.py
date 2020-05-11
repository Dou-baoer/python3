import random
# random is a modul for to inport random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):":
		"Make a class named %%% that is-a %%%.",
	"class %%%(object):\n\tdef __init__(self, ***)":
		"class %%% has-a __int__ that takes self and *** params.",
	"calss %%%(object):\n\tdef ***(self,@@@)":
		"class %%% has-a function *** that takes self and @@@ params.",
	"*** = %%%()":
		"Set *** to a instance of class %%%.",
	"***.***(@@@)":
		"From *** get the *** function, call it with params self, @@@.",
	"***.*** = '***'":
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrasses first
if len(sys.argv) == 2 and sys.argv [1] == "english":
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False

# load up the words from the website
# str.strip() is del the begin and end from the str.
for word in urlopen(WORD_URL).readlines():
	WORDS.append(str(word.strip(), encoding = "utf-8"))

# str.capitalize() is change the first letter from lower case to capital and all of others to lower case.
# .count() is the fuction to count the number of the ().
# random.sample() is to take N element from the first parameter. acount is the second parameter.
def convert(snippet, phrase):
	class_names = [w.capitalize() for w in
					random.sample(WORDS, snippet.count("%%%"))]
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

# range() is diferent from list(). range is return to the object. but list ist return to the list.
# random.randint is to creat a random int.
# str.join is take the ',' in all of the (element)
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(','.join(
			random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

# str.replace(old, new, max)
		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results


# keep going until they hit CTRL-D
try:
	while True:
		snippets = list(PHRASES.keys())
		random.shuffle(snippets)
# random.shuffle() is to mess up the order
# list(dict.keys()) return to a lterate object than use a list function

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print(question)

			input(">")
			print(f"ANSWER:  {answer}\n\n")
except EOFError:
	print("\nBye")
