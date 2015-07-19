#!/usr/bin/env python
import json
import random
import string
import sys

probs = { }
sentence_starters = {}
clause_starters = {}

class Markov_Class:
  def __init__(self):
    return

  def contains_character(__, character_list, word):
    for character in character_list:
      if character in word:
        return True
    return False

  def create_sample_pool(me, word_map):
    sample_pool = []
    for word in word_map.keys():
      count = word_map[word]
      for i in range(count):
        sample_pool.append(word)
    return sample_pool

  def generate_output(self, word_array, output_length, poem):
    sentence_delimiters = [".", "?", "!"]
    clause_delimiters = ["...", ";", "--", ","]
    #word_array = filter(lambda x: x != "", word_array)
    last_word = word_array[0];
    sentence_starters[word_array[0]] = 1;
    # record frequencies / classify words
    for word in word_array:
      if len(last_word) > 0 and last_word[-1] in sentence_delimiters:
        if word not in sentence_starters.keys():
          sentence_starters[word] = 1
        else:
          sentence_starters[word] += 1
      if len(last_word) > 0 and self.contains_character(clause_delimiters, last_word):
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
    generated_list = [random.choice(self.create_sample_pool(sentence_starters))]
    words_on_line = 0
    for i in range(output_length):
      last_word = generated_list[-1]
      next_word = ""
      if self.contains_character(sentence_delimiters, last_word) or last_word not in probs:
        words_on_line +=1
        if self.contains_character(sentence_delimiters, last_word) and poem:
          next_word = "\n"
          words_on_line = 1
        next_word += random.choice(self.create_sample_pool(sentence_starters))
      elif self.contains_character(clause_delimiters, last_word):
        words_on_line += 1
        if poem:
          next_word = "\n"
          words_on_line = 1
        next_word += random.choice(self.create_sample_pool(clause_starters))
      elif last_word in probs:
        words_on_line += 1
        if poem and words_on_line == 10:
          next_word = "\n"
          words_on_line = 1
        next_word += random.choice(self.create_sample_pool(probs[last_word]))
      generated_list.append(next_word)
<<<<<<< HEAD
    # numpy.random.sample(sentence_starters.keys)
    print "\n" * 100
    print(string.join(generated_list, " "))
=======
    for i in range(50):
      print("\n")
    print(" ".join(generated_list))
>>>>>>> e7da3bbe9589224cb80d134edf5d92e44edeb618
