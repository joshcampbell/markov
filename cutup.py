#!/usr/bin/python
import re
import json
import random
import string
import sys

class cutup:
  def generate_output(__, word_array, block_min_size, block_max_size):
    current_position = 0
    chunks = []
    while True:
      next_length = random_chunk_length() 
      next_position = current_position + next_length
      if next_position > len(word_array):
        break
      chunks.append(word_array[current_position:next_position])
      current_position = next_position 
    random.shuffle(chunks)
    chunks = string.join(map(lambda x: string.join(x, " "), chunks), " ")
    print chunks

  def random_chunk_length():
    return random.choice(map(lambda x: x + 1, range(block_min_size, block_max_size)))
