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
  return source_text
