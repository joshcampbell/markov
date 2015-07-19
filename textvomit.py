#!/usr/bin/python
import string
import sys
import argparse
from markov import Markov_Class
from cutup import Cutup_Class

def main():
  parser = argparse.ArgumentParser(description="order of textual operations")
  parser.add_argument("-m", "--markov", help="use markov chains to generate text output of a specified length", type=int)
  parser.add_argument("-c", "--cutup", nargs=2, help="cut up input with cut up block size between X and Y", type=int)
  parser.add_argument("-p", "--poem", help="cut up input with cut up block size between X and Y", action="store_true")
  args = parser.parse_args()
  markov_obj = Markov_Class()
  cutup_obj = Cutup_Class()
  word_array = (clean(take_input()))
  if args.markov:
    output_length = args.markov
<<<<<<< HEAD
    markov_obj.generate_output(word_array, output_length)
  if args.cutup:
    cutup.generate_output(word_array, args.cutup[0], args.cutup[1])
  
=======
    markov_obj.generate_output(word_array, output_length, args.poem)
  if args.cutup:
    cutup_obj.generate_output(word_array, args.cutup[0], args.cutup[1])

>>>>>>> e7da3bbe9589224cb80d134edf5d92e44edeb618
def take_input():
  print('Enter text input below. Hit ctrl-c when done.')
  # sys.stdin.readlines()
  input_lines = []
  try:
    while True:
      input_lines.append(input())
  except KeyboardInterrupt:
      return " ".join(input_lines)

def clean(source_text):
  # fix punctuation
  sentence_delimiters = [".", "?", "!"]
  clause_delimiters = ["...", ";", "--"]
  source_text = source_text.replace("---","--").replace("..", "...").replace("....", "...-")
  for char in (sentence_delimiters + clause_delimiters):
    source_text = source_text.replace(char, char + " ")
  # strip useless characters
  useless = ["\t", "\n", "\"", "\'"]
  for char in useless:
    source_text = source_text.replace(char, "")
  word_array = source_text.split(" ")
  return word_array

if __name__ == "__main__":
    main()
