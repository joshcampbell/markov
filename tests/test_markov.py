import unittest
import string

from unittest import TestCase

from pprint import pprint

from dadapy.markov import MarkovDictionary

class TestTwoWordInput(TestCase):

  def setUp(self):
    self.dictionary = MarkovDictionary()
    self.dictionary.engorge("drink me")

  def test_disgorging_one_word(self):
    output = self.dictionary.disgorge(1)
    output_length = len(output.split(" "))
    self.assertEqual(output_length, 1)

  def test_disgorging_ten_words(self):
    output = self.dictionary.disgorge(10)  
    import ipdb; ipdb.set_trace()
    length = len(output.split(" "))
    self.assertEqual(length, 10)

  def test_length_of_lexicon_is_two(self):
    """
    If a markov dictionary only knows two words, then both of them should appear
    when you retrieve its lexicon.
    """
    length = len(self.dictionary.get_lexicon())
    self.assert_(length == 2)

  def test_first_word_follows_last_word(self):
    """
    To prevent the set of potential next words from ever being empty, we
    consider the first word in the text to follow the last. It follows that the
    output of a markov dictionary that's only been fed two words will consist
    of those two words alternating endlessly.
    """
    output = self.dictionary.disgorge(10) 
    lexicon = self.dictionary.get_lexicon()
    joined_lexicon = lexicon[0] + " " + lexicon[1]
    repeated_lexicon = ""
    for i in range(1,4):
      repeated_lexicon += " " + joined_lexicon
    self.assertNotEqual(output.find(repeated_lexicon), -1, """
      repeated lexicon does not appear in output
      repeated_lexicon:
        %s
      output:
        %s
    """%(repeated_lexicon, output))

