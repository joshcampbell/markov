#!/usr/bin/env python
import re
import json
import random
import string

probs = { }
sentence_starters = {}
clause_starters = {}

def main():
	source_text = """
	Undoubtedly, much of this national mood of hostility to government and business came out of the Vietnam war: its moral shame, its exposure of government lies and atrocities. On top of this came the political disgrace of the Nixon administration in the scandals that came to be known by the one-word label "Watergate," and which led to the historic resignation from the presidency, the first in American history of Richard Nixon in August 1974. The Draco reptoids, usually standing seven to twelve feet tall, have been reported to be the royal elitists of the reptoid hierarchy. They are seen far less often than other reptoids types. The Draco are similar in appearance to the Reptoid, but they have distinct physical differences. Why did Carl Jung, Moses, the Freemasons, the Baptists and so many other groups of people throughout history looked upon the image of a serpent and, through handling the image without fear, represented it as a symbol of our unquestioned love for God and our divine spirituality. Why are dreams of snakes, dragons, lizards or other reptilian animals seem so real and provocative at times?

For almost 200 years, the policy of this Nation has been made under our Constitution by those leaders in the Congress and the White House elected by all of the people. If a vocal minority, however fervent its cause, prevails over reason and the will of the majority, this Nation has no future as a free society.
And now I would like to address a word, if I may, to the young people of this Nation who are particularly concerned, and I understand why they are concerned, about this war. The answer to these questions may be found in the fact that, according to evolutionary science, reptiles were at the root of a genetic matrix from which all land vertebrate life evolved. Millions of years of biological divergence from the trunk of the vertebrate "Tree of Life" resulted in a world full of back boned animals that, despite their dissimilar outward appearance, share the same parental lineage---an encoded past locked in their DNA.  A code which we humans share with other land vertebrate life forms.
	"""
	# fix punctuation
	sentence_delimiters = [".", "?", "!"]
	clause_delimiters = ["...", ";", "--"]
	text_buffer = source_text
	text_buffer = text_buffer.replace("---","--")
	for char in (sentence_delimiters + clause_delimiters):
		text_buffer = text_buffer.replace(char, char+" ")
	# strip useless characters
	useless = ["\t", "\n", "\"", "\'"]
	for char in useless:
		text_buffer = text_buffer.replace(char, "")

	word_array = text_buffer.split(" ")
	word_array = filter(lambda x: x != "", word_array)
	last_word = word_array[0];
	sentence_starters[word_array[0]] = 1;
	# record frequencies / classify words
	for word in word_array:
		if len(last_word) > 0 and last_word[-1] in sentence_delimiters:
			if word not in sentence_starters.keys():
				sentence_starters[word] = 1
			else:
				sentence_starters[word] += 1
		if len(last_word) > 0 and contains_character(clause_delimiters, last_word):
			if word not in clause_starters.keys():
				clause_starters[word] = 1
			else:
				clause_starters[word] += 1
		if not last_word in probs.keys():
			probs[last_word] = {}
			probs[last_word][word] = 1
		else:
			if word not in probs[last_word].keys():
				probs[last_word][word] = 1
			else:
				probs[last_word][word] += 1
		last_word = word
	# generate some text
	# TODO: weighting!
	generated_list = [random.choice(create_sample_pool(sentence_starters))]
	for i in range(100):
		last_word = generated_list[-1]
		next_word = ""
		if last_word in probs:
			next_word = random.choice(create_sample_pool(probs[last_word]))
		else:
			next_word = random.choice(create_sample_pool(sentence_starters))
		generated_list.append(next_word)
	# numpy.random.sample(sentence_starters.keys)
	print(string.join(generated_list, " "))



def contains_character(character_list, word):
	for character in character_list:
		if character in word:
			return True
	return False

def create_sample_pool(word_map):
	sample_pool = []
	for word in word_map.keys():
		count = word_map[word]
		for i in range(count):
			sample_pool.append(word)
	return sample_pool

if __name__ == "__main__":
	main()

# http://stackoverflow.com/questions/16720541/python-string-replace-regular-expression
# line = re.sub(r"(?i)^.*interfaceOpDataFile.*$", "interfaceOpDataFile %s" % fileIn, line)
# https://www.youtube.com/watch?v=xyJJLdaTYTs