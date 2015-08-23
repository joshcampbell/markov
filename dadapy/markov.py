import json
import random
import string
import sys

from Queue import Queue

from dadapy.cleaner import clean

class nGram:
    """ Mutable n-gram class for use in markov dictionaries.
        the idea is that it's filled one word at a time as
        the code consuming it iterates on a list of words.
    """

    def __init__(self, n):
        self.n = n
        self.words = []

    def is_full():
        return len(self.words) == self.n

    def cycle(self, word):
        if self.is_full():
            self.words.remove(self.words[0])
        self.words.append(word)

    def as_key():
        return string.join(self.words)

class MarkovDictionary:
    """ Manages a nested dict of ngramual word occurance probabilities """
    def __init__(self, source_text=None, depth=3, chunk=5):
      # there must be at least depth + 1 words in the source text
      # depth cannot be less than 2
      self.depth = depth
      self.key_length = self.depth - 1
      self.ngrams = {}
      if source_text != None:
        self.engorge(source_text)

    def __is_buffer_full(self, word_buffer):
        return len(word_buffer) == self.depth

    def engorge(self, source_text):
      words = clean(source_text).split()
      word_buffer = []
      for word in words:
          if self.__is_buffer_full(word_buffer):
              word_buffer.remove(word_buffer[0])
          word_buffer.append(word)
          if self.__is_buffer_full(word_buffer):
              self.__upsert_words(word_buffer)
      # the rest of this method is special case handling for the text's end
      # (it links the first word with the final ngram)
      word_buffer.remove(word_buffer[0])
      word_buffer.append(words[0])
      self.__upsert_words(word_buffer)

    def __upsert_words(self, words):
      ngram = string.join(words[0:-1])
      word = words[-1]
      if self.ngrams.get(ngram, None) == None:
          self.ngrams[ngram] = {}
      if self.ngrams[ngram].get(word, None) == None:
          self.ngrams[ngram][word] = 0
      self.ngrams[ngram][word] += 1

    def get_lexicon(self):
      words = []
      for word_dict in self.ngrams.values():
        words += word_dict.keys()
      return words

    def __last_ngram_index(self):
      return -1 * (self.key_length)

    def __last_ngram(self, word_list):
      last_ngram_index = self.__last_ngram_index()
      return word_list[last_ngram_index:]

    def disgorge(self, length=600):
      # TODO: special case handling for length < depth
      word_list = random.choice(self.ngrams.keys()).split()
      for i in range(0, length - self.key_length): 
        if(len(word_list) == self.key_length):
            key = string.join(word_list)
        else:
            key = string.join(self.__last_ngram(word_list))
        followers = self.ngrams[key]
        word_list.append(random.choice(followers.keys()))
      return string.join(word_list)
