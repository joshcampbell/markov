#!/usr/bin/python
import re
import json
import random
import string
import sys

<<<<<<< HEAD
class cutup:
  def generate_output(__, word_array, block_min_size, block_max_size):
=======
class Cutup_Class:
  def generate_output(self, word_array, min_block_size, max_block_size):
>>>>>>> e7da3bbe9589224cb80d134edf5d92e44edeb618
    current_position = 0
    chunks = []
    while True:
      next_length = self.random_chunk_length(min_block_size, max_block_size)
      next_position = current_position + next_length
      if next_position > len(word_array):
        break
      chunks.append(word_array[current_position:next_position])
      current_position = next_position
    random.shuffle(chunks)
    chunks = " ".join(map(lambda x: " ".join(x), chunks))
    for i in range(50):
      print("\n")
    print(chunks)

<<<<<<< HEAD
  def random_chunk_length():
    return random.choice(map(lambda x: x + 1, range(block_min_size, block_max_size)))
=======
  def random_chunk_length(self, min_block_size, max_block_size):
    return random.choice(list(range(min_block_size, max_block_size + 1)))
>>>>>>> e7da3bbe9589224cb80d134edf5d92e44edeb618
