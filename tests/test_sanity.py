import unittest

from unittest import TestCase

from dadapy.markov import MarkovDictionary

class TestSanity(TestCase):
  def setUp(self):
    self.thing = True    

  def test_true(self):
    self.assert_(self.thing)
