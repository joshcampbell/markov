import unittest
import string

from unittest import TestCase

from pprint import pprint

from dadapy.markov import MarkovDictionary

class TestThreeWordInput(TestCase):

  def setUp(self):
    self.dictionary = MarkovDictionary()
    self.source_text = "drink me now."
    self.dictionary.engorge(self.source_text)

  def test_disgorging_one_word(self):
    output = self.dictionary.disgorge(1)
    output_length = len(output.split(" "))
    self.assertEqual(output_length, 1)

  def test_disgorging_ten_words(self):
    output = self.dictionary.disgorge(10)  
    length = len(output.split(" "))
    self.assertEqual(length, 10)

  def test_three_words_in_lexicon(self):
    length = len(self.dictionary.get_lexicon())
    self.assertEqual(length, 3)
