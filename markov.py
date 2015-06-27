#!/usr/bin/env python
import re
import json
import random
import string
import sys

probs = { }
sentence_starters = {}
clause_starters = {}
output_length = 400

def main():
	source_text = string.join(sys.stdin.readlines(), " ")
	# fix punctuation
	sentence_delimiters = [".", "?", "!"]
	clause_delimiters = ["...", ";", "--"]
	text_buffer = source_text
	text_buffer = text_buffer.replace("---","--").replace("..", "...")
	for char in (sentence_delimiters + clause_delimiters):
		text_buffer = text_buffer.replace(char, char + " ")
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
	for i in range(output_length):
		last_word = generated_list[-1]
		next_word = ""
		if contains_character(sentence_delimiters, last_word) or last_word not in probs:
			next_word = random.choice(create_sample_pool(sentence_starters))
		if contains_character(clause_delimiters, last_word):
			next_word = random.choice(create_sample_pool(clause_starters))
		if last_word in probs:
			next_word = random.choice(create_sample_pool(probs[last_word]))
		generated_list.append(next_word)
	# numpy.random.sample(sentence_starters.keys)
	print "\n" * 100
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