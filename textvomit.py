import string
import sys
import argparse
from markov import Markov_Class
from cutup import cutup

def main():
  parser = argparse.ArgumentParser(description="order of textual operations")
  parser.add_argument("-m", "--markov", help="use markov chains to generate text output of a specified length", type=int)
  parser.add_argument("-c", "--cutup", nargs=2, help="cut up input with cut up block size between X and Y", type=int)
  args = parser.parse_args()
  markov_obj = Markov_Class()
  word_array = (clean(take_input()))
  if args.markov:
    output_length = args.markov
    markov_obj.generate_output(word_array, output_length)
  # if args.cutup:
  #   cutup.generate_output(word_array, args.cutup[0], args.cutup[1])
  
def take_input():
  source_text = string.join(sys.stdin.readlines(), " ")
  return source_text

def clean(source_text):
    # fix punctuation
  sentence_delimiters = [".", "?", "!"]
  clause_delimiters = ["...", ";", "--"]
  text_buffer = source_text
  text_buffer = text_buffer.replace("---","--").replace("..", "...").replace("....", "...-")
  for char in (sentence_delimiters + clause_delimiters):
    text_buffer = text_buffer.replace(char, char + " ")
  # strip useless characters
  useless = ["\t", "\n", "\"", "\'"]
  for char in useless:
    text_buffer = text_buffer.replace(char, "")
  word_array = text_buffer.split(" ")
  return word_array

if __name__ == "__main__":
    main()