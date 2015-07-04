#!/usr/bin/env python
import json
import random
import string
import sys

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

def is_markov_node(a_tuple):
    return a_tuple[0] is int and a_tuple[1] is dict

def new_markov_node(count=0):
    return [count, {}]

def dict_of(markov_node):
    return markov_node[1]

def count_of(markov_node):
    return markov_node[0]

def increment(markov_node):
    markov_node[0] += 1

def split_text(text):
    return text.split(" ")

def words_in(markov_node):
    return markov_node[1].keys()

class MarkovDictionary:
    """ Manages a nested dict of contextual word occurance probabilities """
    def __init__(self, *source_texts):
        self.source_texts = source_texts
        self.prob_tree = {}
        for source_text in source_texts:
            self.feed(source_text)

    def engorge(self, source_text):
        last_word = False
        for word in split_text(source_text):
            if last_word is False:
                last_word = word
                continue
            self.__register_word_tuple((last_word, word))
            last_word = word

    def __register_word_tuple(self, word_tuple, depth=2):
        # FIXME needs decomposition
        # TODO implement depth
        if len(word_tuple) is not depth:
            return
        first_word = word_tuple[0]
        second_word = word_tuple[1]
        if first_word in self.prob_tree.keys():
            root_node = self.prob_tree[first_word]
            increment(root_node)
        else:
            root_node = new_markov_node(1)
            self.prob_tree[first_word] = root_node
        if word_tuple[1] in words_in(root_node):
            branch_node = dict_of(root_node)[second_word]
            increment(branch_node)
        else:
            branch_node = new_markov_node(1)
            dict_of(root_node)[second_word] = branch_node

    def disgorge(self, length):
        # sample from the tree, etc.
        return
