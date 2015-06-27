#!/usr/bin/python
import re
import json
import random
import string
import sys

def main():
  source_text = string.join(sys.stdin.readlines(), " ")
  source_text = clean(source_text)
  source_text = source_text.split(" ")
  current_position = 0
  chunks = []
  while True:
    next_length = random_chunk_length() 
    next_position = current_position + next_length
    if next_position > len(source_text):
      break
    chunks.append(source_text[current_position:next_position])
    current_position = next_position 
  random.shuffle(chunks)
  chunks = string.join(map(lambda x: string.join(x, " "), chunks), " ")
  print chunks

def clean(source_text):
    # fix punctuation
  sentence_delimiters = [".", "?", "!"]
  clause_delimiters = ["...", ";", "--"]
  text_buffer = source_text
  text_buffer = text_buffer.replace("---","--").replace("..", "...")
  for char in (sentence_delimiters + clause_delimiters):
    text_buffer = text_buffer.replace(char, char + " ")
  # strip useless characters
  useless = ["\t", "\n", "\"", "\'"]
  for char in useless:
    text_buffer = text_buffer.replace(char, "")
  return text_buffer

def random_chunk_length():
  return random.choice(map(lambda x: x + 1, range(3,8)))

if __name__ == "__main__":
  main()
