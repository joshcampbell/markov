#!/usr/bin/env python2.7
import sys

from argparse import ArgumentParser

from dadapy.markov import MarkovDictionary

def main():
  parser = ArgumentParser(description="specify one or more text transformation:")
  parser.add_argument("-m","--markov", 
                    help="generate n words of markov chain text", 
                    type=int)
  args = parser.parse_args()
  text = sys.stdin.readlines()
  if args.markov:
    length = args.markov
    MarkovDictionary(text).disgorge(length)


if __name__ == "__main__":
    main()
