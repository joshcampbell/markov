import unittest

from unittest import TestCase

from dadapy.markov import MarkovDictionary

class TestMarkovDictionary(TestCase):
  def setUp(self):
    self.dictionary = MarkovDictionary()
  
