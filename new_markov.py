#!/usr/bin/env python2.7
import json
import random
import string
import sys
from pprint import PrettyPrinter

# # Is this a sensible data structure?
#
# <pre>
# {
#   personal: {
#     health: (5, { fund: (1, {bullshit:(1,{})})}
#                   management: (1,{}))
#     problem: (3, {to:(1,{me:(1,{})})})
#     bullshit: (2, {problem:(1,{})})
#   }
# }
# </pre>

TOLERABLE_PUNCTUATION = list(" !.?")

# look, a a big pile of functions pertaining to a
# composite data structure. i wonder how we should
# clean them up ???????

# let's try thinking about it in these terms:

# ProbNode: a list of [int, ProbTree]
#   increment
#   get_subtree
# ProbTree: a dict of { string => ProbNode }
#   random_word
#   upsert_word
#   __insert_word

def is_markov_node(a_tuple):
    return a_tuple[0] is int and a_tuple[1] is dict

def new_markov_node(count=0):
    return [count, {}]

def dict_of(markov_node):
    return markov_node[1]

def dict_as_pairs_of(markov_node):
    return dict_of(markov_node).iteritems()

def count_of(markov_node):
    return markov_node[0]

def increment(markov_node):
    markov_node[0] += 1

def choices(markov_dict):
  words = []
  for tup in dict2list(markov_dict):
    name, markov_node = tup
    count, subdict = markov_node
    for i in range(0,count):
      words.append(name)
  return words 

def register_word(prob_tree, word):
  if word in prob_tree.keys(): increment(prob_tree[word])
  else: prob_tree[word] = new_markov_node(1)
        
# these text tools belong in a namespace

def split_text(text):
    return text.split(" ")

def words_in(markov_node):
    return markov_node[1].keys()

def clean(text):
  return ''.join(letter for letter in text if is_clean(letter))

def is_clean(letter):
  """ isalnum() means "is alphanumeric" """
  return char.isalnum() or char in TOLERABLE_PUNCTUATION

def pprint(text):
  #using defaults for now
  PrettyPrinter().pprint(text)

# these should also be in a module somewhere

dict2list = lambda dic: [(k, v) for (k, v) in dic.iteritems()]
list2dict = lambda lis: dict(lis)

class MarkovDictionary:
    """ Manages a nested dict of contextual word occurance probabilities """
    def __init__(self, *source_texts):
        self.source_texts = []
        self.prob_tree = {}
        for source_text in source_texts:
            self.engorge(source_text)

    def eat_file(self, filename):
       self.engorge(open("./fodder/%s"%filename).read()) 

    def engorge(self, source_text):
        self.source_texts += [source_text]
        last_word = False
        for word in split_text(source_text):
            if last_word is False:
                last_word = word
                continue
            else:
              self.__register_word_tuple((last_word, word))
              last_word = word

    def disgorge(self, length=666):
      first_word = random.choice(self.prob_tree.keys())
      words = [first_word]
      for i in range(1,length+1):
        last_word = words[-1]
        words += [random.choice(choices(dict_of(self.prob_tree[last_word])))]
      return string.join(words, ' ')

    def pretty_print(self, length=666):
        print(disgorge(length))

    def __register_word_tuple(self, word_tuple):
      first_word, second_word = word_tuple
      register_word(self.prob_tree, first_word)
      root_node = dict_of(self.prob_tree[first_word])
      register_word(root_node, second_word)
